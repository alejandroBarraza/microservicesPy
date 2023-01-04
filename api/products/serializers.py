from rest_framework import serializers
from products.models import Product, User
import random
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'image',
            'likes'
        ]
        ReadOnlyFields = ['id']

    
class UserSerializer(serializers.ModelSerializer):
    random_user = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'random_user',
        ]
        ReadOnlyFields = ['random_user']


    def get_random_user(self, obj):
        users = User.objects.all()
        user = random.choice(users)
        return user.id
 
