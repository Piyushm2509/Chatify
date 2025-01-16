from django.urls import path
from .views import signup, login_view, chat_view, logout_view

urlpatterns = [
    path('', signup, name='signup'),  # Redirect root URL to signup
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('chat/', chat_view, name='chat'),
    path('logout/', logout_view, name='logout'),
]
