# File: api/urls.py
from django.urls import path
from .views import PackListView, PackDetailView

urlpatterns = [
    path('packs/', PackListView.as_view(), name='pack-list'),
    path('packs/<str:serial_number>/', PackDetailView.as_view(), name='pack-detail'),
]