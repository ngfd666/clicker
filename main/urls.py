from django.urls import path
from . import views

urlpatterns = [

path("<int:id>",views.index, name="index"),
path('', views.home, name="home"),
path("create/", views.create, name="create"),
path("clicker/", views.clicker, name="clicker"),
path("saveprogress/",views.save_progress,name="saveprogress"),
path("getprogress/",views.get_progress,name="getprogress"),		


]