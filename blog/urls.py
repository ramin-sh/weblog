from . import views
from django.urls import path,re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    re_path(r'detail/(?P<slug>[-\w]+)/', views.PostDetail.as_view(),name='post_detail'),
    path('about/', TemplateView.as_view(template_name="sidebar.html")),


] 
