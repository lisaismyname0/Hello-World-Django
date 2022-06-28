from django.shortcuts import render
from .models import Flavor

def index(request):
    #all views take a request, and here the request is the user visiting a page in the browser
    #you can print(request) if you want
    flavors = Flavor.objects.all
    return render(request, "classes/home.html", {"flavors": flavors})
