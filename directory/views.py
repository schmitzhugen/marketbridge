from django.shortcuts import render
from .models import Doctor, Specialties

def index(request):
	context = {Doctor:Doctor}
	return render(request, 'directory/index.html', context)