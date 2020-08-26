from django.shortcuts import render



# Create your views here.
def home(request):
	return render(request, 'home.html',{})

def contact(request):
	return render(request, 'contact.html',{})

def about(request):
	return render(request, 'about.html',{})

def services(request):
	return render(request, 'services.html',{})

def appointment(request):
	return render(request, 'appointment.html',{})

def pricing(request):
	return render(request, 'pricing.html',{})
