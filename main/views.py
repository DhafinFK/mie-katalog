from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.http import JsonResponse;
import json

from .models import Indomie

from .forms import IndomieForm

# Create your views here.

@login_required(login_url='login')
def show_katalog(request):

    last_login = 'No cookies here'

    if 'last_login' in request.COOKIES:
        last_login = request.COOKIES['last_login']

    context = {
        'mies': Indomie.objects.filter(user=request.user),
        'filtered_by': "",
        "total": Indomie.objects.filter(user=request.user).count(),
        'user': request.user,
        'last_login': last_login,
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


@login_required(login_url='login')
def create_Indomie(request):
    form = IndomieForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        mie_baru = form.save(commit=False)
        mie_baru.user = request.user
        mie_baru.save()
        return HttpResponseRedirect(reverse("mie:katalog"))

    context = {
        'form': form,
    }

    return render(request, "mie_form.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)
            response = HttpResponseRedirect(reverse("mie:katalog"))
            response.set_cookie('last_login', str(datetime.datetime.now()))

            messages.success(request, "Berhasil menambahkan penikmat Indomie!")
            return response

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('mie:katalog')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("mie:katalog"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(
                request, "Maaf, username atau password yang anda masukkan salah.")

    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('login'))
    response.delete_cookie('last_login')
    return response


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


def get_mie_json(request):
    mie_item = Indomie.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', mie_item))


@csrf_exempt
def add_mie_by_ajax(request):
    print("masuk")
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get('amount')
        description = request.POST.get("description")
        price = request.POST.get("price")
        type = request.POST.get("type")

        new_mie = Indomie(user=request.user, name=name, amount=amount,
                          description=description, price=price, type=type)

        new_mie.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


def random(request):
    mie = Indomie.objects.filter(user=request.user).order_by('?').first()

    return JsonResponse({'mie': mie.name})

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Indomie.objects.create(
            user = request.user,
            name = data["name"],
            type = data["type"],
            price = int(data["price"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
