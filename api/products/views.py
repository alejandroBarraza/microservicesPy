from rest_framework import generics
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
    lookup_field = 'pk'

    def create(self, request):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        publish('product_created',serializer.data)
        return Response(serializer.data)

    # def perform_create(self, serializer):
    #     publish()
    #     serializer.save()

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def update(self, request, pk):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        publish('product_updated',serializer.data)
        return Response(serializer.data)
    
    def destroy(self, __, pk):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        publish('product_deleted',pk)
        return Response(serializer.data)


class userAPIView(APIView):
    def get(self, __):
        user = User.objects.all()
        serializer = UserSerializer(user)
        return Response(serializer.data)
        