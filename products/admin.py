
# Register your models here.
from django.contrib import admin
from .models import Product, User
admin.site.register(Product)
admin.site.register(User)