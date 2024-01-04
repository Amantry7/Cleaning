from django.urls import path, include
from .views import index, about, servise, contact
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('services/', servise, name='servise'),
    path('contact/', contact, name='contact'),
    
    
    
    
]
