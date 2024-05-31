from django.urls import path
from .views import note_list, note_detail

urlpatterns = [
    path('', note_list, name='note_list'),
    path('notes/<int:pk>/', note_detail, name='note_detail'),
]