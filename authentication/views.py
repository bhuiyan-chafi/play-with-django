from django.shortcuts import render
from django.http import HttpResponse as response

def signUp(request):
    return render(request,"index.html",{"app_name":"eCommerce App"})
