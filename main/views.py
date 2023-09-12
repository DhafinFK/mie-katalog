from django.shortcuts import render

from .models import Indomie

# Create your views here.

def show_katalog(request):
  context = {
    'mies': Indomie.objects.all(),
    'filtered_by': "",
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