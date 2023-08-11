from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.loginView, name='loginView'),
    path('add_post', views.add_post, name='add_post'),
    path('logout/',views.logoutView),
    path('faramooshi',views.faramooshi),
    path('setpass',views.set_pass),
    path('getmail',views.get_mail),
    path('register',views.register),
    path('/captcha',include("captcha.urls"))
]
