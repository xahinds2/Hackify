from django.urls import path
from . import views

urlpatterns = [
    path('submit/<int:hack_id>', views.submit_data, name='submit_data'),
    path('view_submissions/', views.view_submissions, name='view_submissions'),
]
