from django.contrib import admin
from .models import Task, Product, Order


class ProductAdmin(admin.ModelAdmin):
	list_display = ("product_id", "product_name", "product_count")

admin.site.register(Task)

admin.site.register(Product, ProductAdmin)

admin.site.register(Order)
