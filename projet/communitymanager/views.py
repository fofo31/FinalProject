from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import ConnexionForm
from .models import Communaute


def connexion(request):
    """ Permet à l'utilisateur de se connecter"""

    error = False
    form = ConnexionForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['name']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            id = user.id
            return redirect(communaute, id=id)

        else:
            error = True

    else:
        form = ConnexionForm()
    return render(request, 'connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(connexion)


def communaute(request, id):
    ab = User.objects.get(id=id)
    comm_ab = ab.communaute_set.all()
    comm = Communaute.objects.all()
    pas_ab = []

    for com in comm:
        abonne = False
        for com1 in comm_ab:
            if com.name == com1.name:
                abonne = True
                break
        if not abonne:
            pas_ab.append(com)

    return render(request, 'communaute.html', locals())


def desabonnement(request,id,com_traite):
    ab = User.objects.get(id=id)
    cc = Communaute.objects.get(name=com_traite)
    cc.abonnes.remove(ab)

    return redirect(communaute,id=id)

def abonnement(request,id,com2):
    ab = User.objects.get(id=id)
    cc = Communaute.objects.get(name=com2)
    cc.abonnes.add(ab)

    return redirect(communaute, id=id)

