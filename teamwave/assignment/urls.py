from django.urls import path
from django.views.decorators.cache import cache_page

from .views import GeeksFormView

urlpatterns = [
    path('',cache_page(60*60*24)(GeeksFormView.as_view()),name='search_inputs'),
    path('',GeeksFormView.as_view(),name='search_inputs'),
]
