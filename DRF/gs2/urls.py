from django.urls import path
from . import views


urlpatterns = [
    path('cbv/', views.StudentsView.as_view(), name='cbv_student'),
    path('cbv/<int:pk>/', views.StudentsView.as_view(), name="cbv_edit")
]