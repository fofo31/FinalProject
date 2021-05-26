from django import forms


class ConnexionForm(forms.Form):
    name = forms.CharField(label="Identifiant",required=False)
    password = forms.CharField(label="Mot de Passe",max_length=100,widget=forms.PasswordInput)