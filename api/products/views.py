from rest_framework import viewsets, status
from rest_framework.response import Response
from products.models import Product
from .serializers import ProductSerializer
from django.http import Http404
class ProductView(viewsets.ViewSet):

     # api/product
    def get_object(self,pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def list(self,request):
        products = Product.objects.all()
        serialize = ProductSerializer(products, many=True)
        return Response(serialize.data)

    def create(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        product = self.get_object(pk=pk)
        serialize = ProductSerializer(product)
        return Response(serialize.data)
                    
    def destroy(self,request,pk=None):
        product = self.get_object(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self,request,pk=None):
        product = self.get_object(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_204_NO_CONTENT)

    