from django.shortcuts import render
from front.forms import FeaturesForm

# Create your views here.
def home(request):
    form = FeaturesForm()
    context = {"form": form}
    return render(request, "home/home.html", context)