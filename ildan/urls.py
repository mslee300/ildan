from django.urls import path

from . import views

app_name = "ildan"

urlpatterns = [
  path('', views.index, name='index'),
  path('findtutors/', views.find_tutor, name='find_tutor'),
  path('tutor3/', views.tutor_detail, name='tutor_detail'),
  path('tutor4/', views.tutor_detail2, name='tutor_detail2'),
]