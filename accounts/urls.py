from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.loginView, name='loginView'),
    path('add_post/<int:post_id>', views.add_post, name='add_post'),
    path('add_newpost', views.add_newpost, name='add_newpost'),
    path('logout/',views.logoutView),
    path('faramooshi',views.faramooshi),
    path('setpass',views.set_pass),
    path('getmail',views.get_mail),
    path('register',views.register),
    path('show_post',views.show_post),
    path('/captcha',include("captcha.urls"))
]
