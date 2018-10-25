from django.urls import path
# from . import views
from .views import *

urlpatterns = [
    path('main/', main, name='main'),
    path('show/', show)
    # ctrl + d 한줄복사
]
