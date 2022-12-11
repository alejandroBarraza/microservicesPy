from django.urls import path
from .views import ProductView
urlpatterns = [
    path('products', ProductView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductView.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'put' : 'update'
    }))
]
