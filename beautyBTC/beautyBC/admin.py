from django.contrib import admin

from beautyBC.models import Category, Mark, Products, Providers, Purchases, Stock, Sales

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category)
admin.site.register(Mark)
admin.site.register(Products)
admin.site.register(Providers)
admin.site.register(Purchases)
admin.site.register(Stock)
admin.site.register(Sales)
