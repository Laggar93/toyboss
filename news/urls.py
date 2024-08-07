from django.urls import path
from . import views


urlpatterns = [
    path('news/', views.news_page_view, name='news_page'),
    path('news/<str:news_item_slug>/', views.news_view_detail, name='news_items'),
]