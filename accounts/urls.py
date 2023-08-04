from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show', views.show_post, name='show'),
    path('logout/',views.logoutView),
    path('faramooshi',views.faramooshi),
    path('setpass',views.set_pass),
    path('getmail',views.get_mail),
    path('register',views.register),
]