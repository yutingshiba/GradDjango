from django.urls import path

from .views import SignUpView, LogInView, LogOutView

urlpatterns = [
    path('signup', SignUpView.as_view()),
    path('login', LogInView.as_view()),
    path('logout', LogOutView.as_view()),
]
