from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("sandeep_sharma/", views.sandeep_sharma, name="sandeep_sharma"),
    path("amit_mishra/", views.amit_mishra, name="amit_mishra"),
    path("travis_head/", views.travis_head, name="travis_head"),
]