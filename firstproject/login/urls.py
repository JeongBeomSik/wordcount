
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.login, name='login'),
    path('check/', views.check, name='check'),

]