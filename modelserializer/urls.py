from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfoclass/', views.StudentAPI.as_view())
]
