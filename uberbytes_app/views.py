from django.shortcuts import render

# Create your views here.
# Acts like rails controller.

def home(request):
    return render(request, "home.html", {})
