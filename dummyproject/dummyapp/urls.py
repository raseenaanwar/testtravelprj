from . import views
from django.urls import path
urlpatterns = [
    path('',views.home1,name='home1'),
]
