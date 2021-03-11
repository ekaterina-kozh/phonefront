from django.urls import path, include

from app.user.views import UserByToken

urlpatterns = [
    path('user/by/token', UserByToken.as_view()),
]
