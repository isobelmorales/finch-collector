# path function is used to define each route
from django.urls import path
from . import views

# holds each route defined for main_app
urlpatterns = [
    # displays the Home page
    path('', views.home, name='home'),
]