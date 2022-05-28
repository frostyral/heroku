from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='stsm-home'),
    path('register/', views.register, name='stsm-register'),
    path('admitted-list/', views.display, name='stsm-display'),
]
