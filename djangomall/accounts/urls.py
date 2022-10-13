from django.contrib import admin
from django.urls import path
from accounts import views
from djangomall.urls import NewLoginView

urlpatterns = [
    
    path('signup/', views.signup),
    path('login/', NewLoginView.as_view()),

    path('oauth_login/', views.oauth_login),
    path('oauth_callback/', views.oauth_callback),

]


