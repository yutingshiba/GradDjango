from django.urls import path

from .views import CreateUserView, GetTokenView

urlpatterns = [
    path('createUser/', CreateUserView.as_view()),
    path('getToken/', GetTokenView.as_view()),
]
