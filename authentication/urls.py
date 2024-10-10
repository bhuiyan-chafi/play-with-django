from django.urls import path
from . import views

#the name should be always urlspatterns otherwise Django will not recongnize this. You will face a NameError
#you should always put / at the end of the path not before, otherwise the route will be recongnised 
urlpatterns = [
    path('signup/',views.signUp)
]