from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.loginView, name='loginView'),
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
    path('add_newpost', views.add_newpost, name='add_newpost'),
    path('logout/',views.logoutView),
    path('faramooshi',views.faramooshi),
    path('setpass',views.set_pass),
    path('getmail',views.get_mail),
    path('register',views.register),
    path('show_post',views.show_post, name='show_post'),
    path('/captcha',include("captcha.urls")),
    path('get_background',views.get_background),#TODO badan takmil shavad
]
