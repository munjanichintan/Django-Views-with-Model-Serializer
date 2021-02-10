from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
	def get(self, request, *args, **kwargs):
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id', None)
		if id is not None:
			stu = Student.objects.get(id=id)
			serializer = StudentSerializer(stu)
			# json_data = JSONRenderer().render(serializer.data)
			# return HttpResponse(json_data, content_type='application/json')
			return JsonResponse(serializer.data)
		stu = Student.objects.all()
		serializer = StudentSerializer(stu, many=True)
		# json_data = JSONRenderer().render(serializer.data)
		# return HttpResponse(json_data, content_type='application/json')
		return JsonResponse(serializer.data, safe=False)

	def post(self, request, *args, **kwargs):
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		serializer = StudentSerializer(data=pythondata)
		if serializer.is_valid():
			serializer.save()
			res = {'msg': 'Record Created Successfully'}
			return JsonResponse(res)
		return JsonResponse(serializer.errors)

	def put(self, request, *args, **kwargs):
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id')
		stu = Student.objects.get(id=id)
		serializer = StudentSerializer(stu, data=pythondata, partial=True)
		if serializer.is_valid():
			serializer.save()
			res = {'msg': 'Data Updated'}
			return JsonResponse(res)
		return JsonResponse(serializer.errors)

	def delete(self, request, *args, **kwargs):
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id')
		stu = Student.objects.get(id=id)
		stu.delete()
		res = {'msg': 'Delete Successfully'}
		return JsonResponse(res)