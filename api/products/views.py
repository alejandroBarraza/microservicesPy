from rest_framework import generics, status
from rest_framework.views import APIView
from products.models import Product, User
from .serializers import ProductSerializer, UserSerializer
# from django.http import Http404
from rest_framework.response import Response
from products.producer import publish

# create product model or list of the products ( get, post)
class ProductListCraeteAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        publish('product_created',response.data)
        return response

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def update(self, request, pk):
        response = super().update(request, pk)
        publish('product_updated',response.data)
        return response
    
    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        publish('product_deleted',obj.id)
        return super().destroy(request, *args, **kwargs)


class userAPIView(APIView):
    def get(self, __):
        user = User.objects.all()
        serializer = UserSerializer(user)
        return Response(serializer.data)
        