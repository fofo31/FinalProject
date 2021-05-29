from . import views
from django.urls import path

urlpatterns = [
    path('connexion/',views.connexion, name='connexion'),
    path('communaute/<int:id>',views.communaute,name='communaute'),
    path('communaute/deconnexion/',views.deconnexion,name='deconnexion'),
    path('communaute/desabonnement/<int:id>/<str:com_traite>',views.desabonnement,name='desabonnement'),
    path('communaute/abonnement/<int:id>/<str:com2>',views.abonnement,name='abonnement'),
    path('afficher_communaute/<int:id>',views.afficher_communaute,name='afficher_communaute'),
    path('voir_post/<int:id>',views.voir_post,name='voir_post')
]