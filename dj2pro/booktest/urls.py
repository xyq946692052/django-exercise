from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('temp_var/', views.temp_var),
    path('temp_tag/', views.temp_tag),
    path('temp_filter/', views.temp_filter),
    path('login', views.login),
    path('login_check', views.login_check),
    path('change_pwd', views.change_pwd),
    path('change_pwd_action', views.change_pwd_action),
    path('verify_code', views.verify_code),
    path('show_upload', views.show_upload),
    path('upload_handle', views.upload_handle),
    path('show_area/<int:num>', views.show_area),
]
