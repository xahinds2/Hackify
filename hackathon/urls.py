from hackathon import views
from django.urls import path

urlpatterns = [
    path('create/', views.create, name='create'),
    path('hackathons/', views.hackathons, name='hackathons'),
    path('register_hack/', views.register_hack, name='register_hack'),
    path('my_hackathons/', views.my_hackathons, name='my_hackathons'),
    path('register_hack/<int:hack_id>/', views.register_hack, name='register_hack'),
]
