from django.shortcuts import render
from gs1.serializers import StudentModelSerializer
from gs1.models import Student
from rest_framework import generics

# Create your views here.

class stl_view(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class stc_view(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class str_view(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class stu_view(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class std_view(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class stlc_view(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class stru_view(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class strd_view(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

class stlc_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer