from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.showPosts),
    path("addpost/", views.addPost, name="addpost"),
    path("updatepost/<int:pk>/", views.updatePost, name="updatepost"),
    path("posts/", views.showPosts, name="posts"),
    path('deletepost/<int:pk>/', views.deletePost, name='deletepost'),
    path('regist/', views.register, name="regist"),
    path('login/', views.loginOperation, name="login"),
    path('logout/', views.logoutOperation, name="logout"),
    path('message/', views.message, name="message"),
    path('deletemessage/<int:pk>/', views.deleteMessage, name="deletemessage")

]
