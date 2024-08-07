from django.urls import path
from . import views


urlpatterns = [
    path('production/', views.production_view, name='production_page'),

]