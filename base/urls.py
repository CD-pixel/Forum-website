from django.urls import path
from . import views



urlpatterns =[

    path('', views.forum, name="forum"),
    path('thread/<id>', views.thread, name="thread"),
    path('new-thread/', views.newThread, name="new-thread"),
    path('register/', views.registerUser, name="register"),
    path('login/', views.loginUser, name="login")

]