from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import ConnexionForm

def accueil(request):
    return render(request,'accueil.html',locals())


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
            return redirect(accueil)

        else:
            error=True

    else:
        form = ConnexionForm()
    return render(request, 'connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(connexion)


