from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.products_view, name='products_page'),

]