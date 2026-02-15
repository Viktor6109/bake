from django.urls import path
from . import views


app_name = 'goods'
urlpatterns = [
    path('product/<slug:product_slug>/', views.product, name='product'),
    path('<slug:category_slug>/', views.catalog, name='catalog'),
]
