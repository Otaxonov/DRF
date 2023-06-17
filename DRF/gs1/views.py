from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer, StudentModelSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Student
import io


# Create your views here.


def StudentsView(request):
    
    students = Student.objects.all()
    serializer = StudentModelSerializer(students, many=True)
    
    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type="application/json")


def StudentDetailView(request, pk):
    student = Student.objects.get(pk=pk)
    serializer = StudentSerializer(student)

    return JsonResponse(serializer.data)

@csrf_exempt
def StudentCreateView(request):

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)

        if serializer.is_valid():
            serializer.save()
            res = {"message": "Data Created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
    
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type="application/json")
