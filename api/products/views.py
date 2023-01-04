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

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        publish()
        return Response(serializer.data)

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class userAPIView(APIView):
    def get(self, __):
        user = User.objects.all()
        serializer = UserSerializer(user)
        return Response(serializer.data)
        