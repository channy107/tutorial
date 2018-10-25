
from django.contrib import admin
from django.urls import path, include
from firstapp import views

urlpatterns = [
    path('ex1/', views.ex1),
    path('ex2/', views.ex2),
    path('template/', views.template),
    path('admin/', admin.site.urls),
    path('index1/', views.index1),
    path('index2/', views.index2),
    path('first/', include('firstapp.urls')),
]
