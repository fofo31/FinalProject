from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

class Communaute(models.Model):
    name = models.CharField(max_length=200)
    abonnes = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Priorite(models.Model):
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label

class Post(models.Model):
    description = models.CharField(max_length=200)
    #titre=models.CharField(max_length=200)
    date = models.DateField()
    communaute = models.ForeignKey('Communaute',on_delete=models.CASCADE)
    priorite = models.ForeignKey('Priorite', on_delete=models.CASCADE)
    evenementiel = models.BooleanField(default=False)
    date_evenement=models.DateField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)

class Commentaire(models.Model):
    date_creation = models.DateField(default=timezone.now())
    contenu = models.CharField(max_length=200)
    auteur_commentaire = models.ForeignKey(User, on_delete=models.CASCADE)
    post_commente = models.ForeignKey(Post,on_delete=models.CASCADE)


