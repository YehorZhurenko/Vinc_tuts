from django.urls import path
from .views import *


urlpatterns = [
    path('', homePageView, name = 'home'),
    path('alt/', altHomePage, name = 'altHome'),

]