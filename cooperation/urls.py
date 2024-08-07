from django.urls import path
from . import views


urlpatterns = [
    path('cooperation/', views.cooperation_view, name='cooperation_page'),

]