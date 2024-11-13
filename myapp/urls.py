from django.urls import path
from . import views

urlpatterns = [
    path('', views.person_create, name='home'),  # 根路径的路由，指向填写表单页面
    path('person/add/', views.person_create, name='person_create'),
    path('person/success/', views.person_success, name='person_success'),
]
