from django.urls import path
from .views import chat_view, delete_all

urlpatterns = [
    path('chat/', chat_view, name='chat'),
    path('chat/delete_all/', delete_all, name='delete all')
]