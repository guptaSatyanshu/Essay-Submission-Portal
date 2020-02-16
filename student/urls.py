from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('', views.register, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.logout_views, name='logout'),
]
