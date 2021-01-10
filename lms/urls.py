from django.urls import path
from . import views


app_name = 'lms'
urlpatterns = [
    path('', views.home, name='home'),
    path('students', views.StudentsList.as_view(), name='students'),

]
