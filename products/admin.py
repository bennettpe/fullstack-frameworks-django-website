from django.contrib import admin
from .models import Product

# ADD columns to Django Admin Model Pages
# How to Add Columns to Django Admin Model Pages (Django Tutorial) | Part 38
# https://www.youtube.com/watch?v=KqbvhPLGJwA&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=38
class ProductAdmin(admin.ModelAdmin):
    list_display =('category','part_name', 'part_number')
    
    def user_info(self, obj):
        return obj.description
        
    # How to Customise Object Sort Order in Django Admin Pages (Django Tutorial) | Part 39   
    # https://www.youtube.com/watch?v=j-CCNJmZQ6c&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=39
    # Sort order in Django Admin Model Pages    
    def get_queryset(self, request):
        queryset = super(ProductAdmin, self).get_queryset(request)
        queryset = queryset.order_by('category', '-part_name', 'part_number')
        return queryset

# Register your models here.
admin.site.register(Product, ProductAdmin)