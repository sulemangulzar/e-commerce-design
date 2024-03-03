from django.http import HttpResponse
from django.shortcuts import render

def HomePage(request):
    return render(request,"index.html",)
def CartPage(request):
    return render(request,"cart.html",)
def aboutUs(request):
    return HttpResponse("About Us Page")
def ContactUs(request):
    return HttpResponse("Contact Page")
def Content(request, content):
    return HttpResponse(content)



