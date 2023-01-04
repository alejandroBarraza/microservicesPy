from django.urls import path
from .views import ProductListCraeteAPIView, ProductRetrieveUpdateDestroyAPIView,userAPIView

urlpatterns = [
        path('products/', ProductListCraeteAPIView.as_view(), name='product-list'),
        path('products/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
        path('user/', userAPIView.as_view(), name='user')
    ]
    

