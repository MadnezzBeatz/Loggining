from django.contrib.auth import login
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import Steam
from .forms import SteamForm
from .scripts import code
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zak.zak.settings")


def accounts_home(request):
    accs = Steam.objects.all()
    return render(request, 'accounts/accounts_home.html', {'accs': accs})

def add_accounts(request):
    error =''
    if request.method == 'POST':
        form = SteamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else: error= 'форма не верная'


    form = SteamForm()
    data = {
        'form':form
    }
    return render(request, 'accounts/add_accounts.html', data)

def log_to_acc(request):

    # launcher = request.GET.get("launcher",0)
    gamename = request.GET.get('gamename',0)
    gameclub = request.GET.get('gameclub',0)


    account =  code.get_accounts(gamename, gameclub)


    return JsonResponse(account, safe=False, encoder=DjangoJSONEncoder)

def get_game(request):
    resp = code.get_games()
    return JsonResponse(resp, safe=False, encoder=DjangoJSONEncoder)


def change_status_false(request):
    # launcher = request.GET.get("launcher",0)
    login = request.GET.get("login",0)
    resp = code.change_status_false(login)

    # return HttpResponse(f"{resp}")

def change_status_true(request):
    # launcher = request.GET.get("launcher",0)
    login = request.GET.get("login",0)
    resp = code.change_status_true(login)

    # return HttpResponse(f"{resp}")



# Create your views here.
