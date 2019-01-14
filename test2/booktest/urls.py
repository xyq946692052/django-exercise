from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books$', views.books),
    url(r'^create', views.create),
    url(r'^delete/(\d+)', views.delete),
    url(r'^areas$', views.areas),
]
