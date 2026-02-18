from .views import *
from django.urls import path

urlpatterns = [
    path('', messageboard_view, name="messageboard"),
    path('subscribe/', subscribe, name="subscribe"),
    path('newsletter/',newsletter,name="newsletter")
    
]