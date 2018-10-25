from django.urls import path
# from . import views
from .views import *

urlpatterns = [
    path('main/', main, name='main'),
    path('show/', show),
    path('insert', insert),
    # ctrl + d 한줄복사

]
