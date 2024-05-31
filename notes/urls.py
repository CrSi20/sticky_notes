from django.urls import path
from .views import note_list, note_detail, note_update

urlpatterns = [
    path('', note_list, name='note_list'),
    path('note/<int:pk>/', note_detail, name='note_detail'),
    path('note/<int:pk>/edit/', note_update, name='note_update'),
]