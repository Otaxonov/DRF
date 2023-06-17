from django.urls import path
from . import views

urlpatterns = [
    path('stl/', views.stl_view.as_view()),
    path('stc/', views.stc_view.as_view()),
    path('str/<int:pk>', views.str_view.as_view()),
    path('stu/<int:pk>', views.stu_view.as_view()),
    path('std/<int:pk>', views.std_view.as_view()),
]