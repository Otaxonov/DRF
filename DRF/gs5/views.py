from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from gs1.models import Student
from gs1.serializers import StudentModelSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class StudentViewSet(viewsets.ViewSet):
    
    def list(self, request):
        students = Student.objects.all()
        serializer = StudentModelSerializer(students, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = StudentModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            res = {"message": "Data Created"}

            return Response(res, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        if pk is not None:
            student = Student.objects.get(pk=pk)
            serializer = StudentModelSerializer(student)
            return Response(serializer.data)
        
        students = Student.objects.all()
        
        serializer = StudentModelSerializer(students, many=True)
        
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        student = Student.objects.get(pk=pk)

        serializer = StudentModelSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            res = {"message": "Data Updated"}
            return Response(res)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        student = Student.objects.get(pk=pk)

        serializer = StudentModelSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            res = {"message": "Partial Data Updated"}
            return Response(res)
        
        return Response(serializer.errors)
    
    def destroy(self, request, pk=None):
        student = Student.objects.get(pk=pk)

        student.delete()

        res = {"message": "Data Deleted"}

        return Response(res)
    

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer