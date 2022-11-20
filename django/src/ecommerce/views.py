from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
        context={
            "title":"HOME"
        }
        return render(request, "home.html", context)

def about_page(request):
        context={
            "title":"ABOUT"
        }
        return render(request, "home.html", context)

def contact_page(request):
        contact_form = ContactForm(request.POST or None)

        if contact_form.is_valid():
            print(contact_form.cleaned_data)
        if request.method == "POST":
            print(request.POST.get("fullname"))

        return render(request, "contact/view.html", {'form' : contact_form})
