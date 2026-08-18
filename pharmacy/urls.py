from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('search/', views.search_view, name='search'),
    path('upload/', views.upload_prescription_view, name='upload_prescription'),
    path('checkout/<int:medicine_id>/', views.checkout_view, name='checkout'),
]
