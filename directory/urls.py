from django.urls import path, include
from . import views

app_name = "directory"
urlpatterns = {
	path('', views.index, name="index")
}