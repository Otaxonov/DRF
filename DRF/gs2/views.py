from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from gs1.models import Student
from gs1.serializers import StudentModelSerializer


# Create your views here.

class StudentsView(APIView):
    def get(self, request, pk=None, format=None):

        if pk is not None:
            student = Student.objects.get(pk=pk)
            serializer = StudentModelSerializer(student)
            return Response(serializer.data)
        
        students = Student.objects.all()
        
        serializer = StudentModelSerializer(students, many=True)
        
        return Response(serializer.data)
    
    def post(self, request, format=None):
        
        serializer = StudentModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            res = {"message": "Data Created"}

            return Response(res, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):

        student = Student.objects.get(pk=pk)

        serializer = StudentModelSerializer(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            res = {"message": "Data Updated"}
            return Response(res)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):

        student = Student.objects.get(pk=pk)

        serializer = StudentModelSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            res = {"message": "Partial Data Updated"}
            return Response(res)
        
        return Response(serializer.errors)
    
    def delete(self, request, pk, format=None):
        
        student = Student.objects.get(pk=pk)

        student.delete()

        res = {"message": "Data Deleted"}

        return Response(res)

