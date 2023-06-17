from django.shortcuts import render
from rest_framework import mixins, generics
from gs1.models import Student
from gs1.serializers import StudentModelSerializer

# Create your views here.

class StudentsListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class student_create_view(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class student_retrieve_view(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    

class student_update_view(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    

class student_delete_view(mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)