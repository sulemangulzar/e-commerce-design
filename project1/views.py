from django.http import HttpResponse
from django.shortcuts import render

def HomePage(request):
    return render(request,"index.html",)
def CartPage(request):
    return render(request,"cart.html",)




