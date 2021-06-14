from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ConnexionForm, NouveauPost, NouveauCommentaire
from .models import Communaute, Post, Commentaire


def connexion(request):
    """ Permet à l'utilisateur de se connecter"""

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
    '''Permet à l'utilisateur de se déconnecter'''
    logout(request)
    return redirect(connexion)


@login_required
def communaute(request, id):
    '''Affiche toutes les communautés avec la possibilité de s'abonner/se désabonner'''
    current_user = User.objects.get(id=id)
    user_communities = current_user.communaute_set.all()
    all_communities = Communaute.objects.all()
    not_subscribed = [] #liste des communautés auxquelles l'utilisateur n'est pas abonné

    for com in all_communities:
        abonne = False
        for com1 in user_communities:
            if com.name == com1.name:
                abonne = True
                break
        if not abonne:
            not_subscribed.append(com)

    return render(request, 'communaute.html', locals())


@login_required
def desabonnement(request, id, com_traite):
    ab = User.objects.get(id=id)
    cc = Communaute.objects.get(name=com_traite)
    cc.abonnes.remove(ab)

    return redirect(communaute, id=id)


@login_required
def abonnement(request, id, com2):
    ab = User.objects.get(id=id)
    cc = Communaute.objects.get(name=com2)
    cc.abonnes.add(ab)

    return redirect(communaute, id=id)

@login_required
def afficher_communaute(request, id):
    '''Affiche tous les posts d'une communauté'''
    comm_affichee = get_object_or_404(Communaute, id=id)
    posts = comm_affichee.post_set.all()

    return render(request, 'afficher_communaute.html', locals())

@login_required
def voir_post(request,post_id):
    '''Affiche les détails du post dont l'id est post_id'''
    post_affiche = get_object_or_404(Post, id=post_id)
    commentaires_post = post_affiche.commentaire_set.all()
    return render(request,'voir_post.html',locals())

@login_required
def nouveau_post(request):
    '''Permet de créer un nouveau post'''
    form = NouveauPost(request.POST or None)
    if form.is_valid():
        description = form.cleaned_data['description']
        date = form.cleaned_data['date']
        communaute = form.cleaned_data['communaute']
        priorite = form.cleaned_data['priorite']
        evenementiel = form.cleaned_data['evenementiel']
        date_evenement = form.cleaned_data['date_evenement']
        auteur = form.cleaned_data['auteur']
        Post(description=description,date=date,communaute=communaute,priorite=priorite,evenementiel=evenementiel,date_evenement=date_evenement,auteur=auteur).save()
        new_post = get_object_or_404(Post,description=description)
        return redirect('voir_post', post_id=new_post.id)

    return render(request,'nouveau_post.html',locals())

@login_required
def nouveau_commentaire(request, post_id):
    '''Permet de créer un nouveau commentaire'''
    post = get_object_or_404(Post,id=post_id)
    form = NouveauCommentaire(request.POST or None)
    if form.is_valid():
        contenu = form.cleaned_data['contenu']
        Commentaire(contenu=contenu,auteur_commentaire=request.user,post_commente=post).save()
        return redirect('voir_post',post_id=post_id)
    return render(request,'ajouter_commentaire.html',locals())

@login_required
def modif_post(request,post_id):
    '''Permet de modifier un post'''
    post=get_object_or_404(Post,id=post_id)
    autorisation = False
    if post.auteur == request.user:
        autorisation = True
    form = NouveauPost(request.POST or None)
    form.fields['description'].initial = post.description
    form.fields['date'].initial = post.date
    form.fields['communaute'].initial = post.communaute
    form.fields['priorite'].initial = post.priorite
    form.fields['evenementiel'].initial = post.evenementiel
    form.fields['date_evenement'].initial = post.date_evenement
    form.fields['auteur'].initial = post.auteur
    form.fields['titre'].initial = post.titre
    if form.is_valid():
        titre = form.cleaned_data['titre']
        description = form.cleaned_data['description']
        date = form.cleaned_data['date']
        communaute = form.cleaned_data['communaute']
        priorite = form.cleaned_data['priorite']
        evenementiel = form.cleaned_data['evenementiel']
        date_evenement = form.cleaned_data['date_evenement']
        auteur = form.cleaned_data['auteur']
        post.titre = titre
        post.description = description
        post.date = date
        post.communaute = communaute
        post.priorite = priorite
        post.evenementiel= evenementiel
        post.date_evenement = date_evenement
        post.auteur = auteur
        post.save()

        return redirect('voir_post',post_id=post.id)
    return render(request,'modifier_post.html',locals())

