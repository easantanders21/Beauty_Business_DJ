from django.contrib import admin

from beautyBC.models import Category, Mark, Products, Providers, Purchases, Stock, Sales

class CategoryAdmin(admin.ModelAdmin):
    list_display=("category_id", "name_category")

class MarkAdmin(admin.ModelAdmin):
    list_display=("mark_id", "name_name")

class ProductsAdmin(admin.ModelAdmin):
    list_display=("mark_id", "name_mark")

class ProvidersAdmin(admin.ModelAdmin):
    list_display=("provider_name", "phone", "provider_address")

class PurchaseAdmin(admin.ModelAdmin):
    list_display=("provider", "purchase_date", "factura")

class StockAdmin(admin.ModelAdmin):
    list_display=("purchase", "product", "purchase_price", "sales_price", "amount", "sales_st")

class SalesAdmin(admin.ModelAdmin):
    list_display=("sale_date", "stock_ref", "amount")

admin.site.register(Category, CategoryAdmin)
admin.site.register(Mark, MarkAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Providers, ProvidersAdmin)
admin.site.register(Purchases, PurchaseAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Sales, SalesAdmin)
