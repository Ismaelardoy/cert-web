from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'CertwebAPP/home.html')

def services(request):
    return render(request, 'CertwebAPP/services.html')

def about_me(request):
    return render(request, 'CertwebAPP/about_me.html')