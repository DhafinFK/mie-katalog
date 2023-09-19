from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers
from django.contrib import messages

from .models import Indomie

from .forms import IndomieForm

# Create your views here.

def show_katalog(request):
  context = {
    'mies': Indomie.objects.all(),
    'filtered_by': "",
    "total": Indomie.objects.count(),
  }

  if request.method == 'POST':
    selected_category = request.POST.get('filter_category')

    if selected_category == "MG":
      context['mies'] = Indomie.objects.filter(type="MG")
      context['filtered_by'] = "Indomie Goreng"
    
    elif selected_category == "MK":
      context['mies'] = Indomie.objects.filter(type="MK")
      context['filtered_by'] = "Indomie Kuah"

    elif selected_category == "HU":
      context['mies'] = Indomie.objects.order_by("price").reverse()
      context['filtered_by'] = "Harga Tertinggi"

    elif selected_category == "HL":
      context['mies'] = Indomie.objects.order_by("price")
      context['filtered_by'] = "Harga Terendah"

    else:
      context['mies'] = Indomie.objects.all()
      context['filtered_by'] = ""

    

  return render(request, "katalog.html", context)

def create_Indomie(request):
  form = IndomieForm(request.POST or None)

  if form.is_valid() and request.method == "POST":
    form.save()
    return HttpResponseRedirect(reverse("mie:katalog"))
  
  context = {
    'form': form,
  }

  return render(request, "create_mie.html", context)

def show_xml(request):
  data = Indomie.objects.all()
  return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
  data = Indomie.objects.filter(pk=id)
  return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
  data = Indomie.objects.all()
  return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
  data = Indomie.objects.filter(pk=id)
  return HttpResponse(serializers.serialize("json", data), content_type="application/json")