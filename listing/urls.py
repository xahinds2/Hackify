from listing import views
from django.urls import path

urlpatterns = [
    path('cart_view/', views.cart_view, name='cart_view'),
    path('hackathons/', views.hackathons, name='hackathons'),
    path('register_hack/', views.register_hack, name='register_hack'),
    path('register_hack/<int:hack_id>/', views.register_hack, name='register_hack'),
]
