from django.urls import path
from .views import StudentsView, StudentDetailView, StudentCreateView

urlpatterns = [
    path('students/', StudentsView, name='students'),
    path('student/<int:pk>/', StudentDetailView, name='student'),
    path('student/create/', StudentCreateView, name='student_create')
]