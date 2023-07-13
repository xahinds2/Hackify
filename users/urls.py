from users import views
from django.urls import path

urlpatterns = [
    path('view_hacks/', views.view_hacks, name='view_hacks'),
    path('signup/', views.signup, name='signup'),
    path("login/", views.login, name="login")
]
