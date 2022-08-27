from django.shortcuts import render
from .models import Listings

def index(request):
	context = {Listings:Listings}
	return render(request, 'directory/index.html', context)