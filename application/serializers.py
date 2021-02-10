from .models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):

	def start_with_c(value):
		if value[0] == value[0].lower():
			raise serializers.ValidationError('First letter should be Capital')

	name = serializers.CharField(validators=[start_with_c])
	class Meta:
		model = Student
		fields = ['id', 'name', 'roll', 'city']
		# read_only_fields = ['name', 'roll']
		# extra_kwargs = {'name': {'read_only':True}}