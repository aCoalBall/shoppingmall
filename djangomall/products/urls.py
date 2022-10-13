from django.urls import path

from . import views

urlpatterns = [
    path('categories/<category_id>/', views.get_category, name='get_category'),
    path('<product_id>/', views.get_product, name='get_product'),
]

