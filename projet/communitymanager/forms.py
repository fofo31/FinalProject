from django import forms

from .models import Post, Commentaire


class ConnexionForm(forms.Form):
    name = forms.CharField(label="Identifiant", required=False)
    password = forms.CharField(label="Mot de Passe", max_length=100, widget=forms.PasswordInput)


class NouveauPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class NouveauCommentaire(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('contenu',)
