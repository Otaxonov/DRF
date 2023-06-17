from django.urls import path
from .views import (
    StudentsListView,
    student_create_view,
    student_retrieve_view,
    student_update_view,
    student_delete_view
)

urlpatterns = [
    path('stl/', StudentsListView.as_view(), name='ctu'),
    path('stc/', student_create_view.as_view()),
    path('str/<int:pk>', student_retrieve_view.as_view()),
    path('stu/<int:pk>', student_update_view.as_view()),
    path('std/<int:pk>', student_delete_view.as_view()),
]

