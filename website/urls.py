from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.displayAll, name="home"),
    path('post/<int:pk>/', views.displayPost, name='post'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),

]
