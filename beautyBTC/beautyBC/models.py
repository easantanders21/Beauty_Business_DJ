# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the
#     desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create,
#     modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field
#     names.
from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name_category = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'category'

    def __str__(self):
        return self.name_category


class Mark(models.Model):
    mark_id = models.AutoField(primary_key=True)
    name_mark = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'mark'
    
    def __str__(self):
        return self.name_mark


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name_product = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'products'

    def __str__(self):
        return "{} {} {}".format(self.name_product, self.category, self.mark)

        
class Providers(models.Model):
    provider_id = models.AutoField(primary_key=True)
    provider_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=25)
    provider_address = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'providers'

    def __str__(self):
        return "{} {} {}".format(self.provider_name, self.phone, self.provider_address)


class Purchases(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    provider = models.ForeignKey(Providers, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    factura = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'purchases'

    def __str__(self):
        return "{} {} {}".format(self.provider, self.purchase_date, self.factura)


class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    purchase = models.ForeignKey(Purchases, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    purchase_price = models.IntegerField()
    sales_price = models.IntegerField()
    amount = models.IntegerField()
    sales_st = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock'

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.product, self.product, self.purchase_price, self.sales_price, self.amount, self.sales_st)


class Sales(models.Model):
    sale_id = models.AutoField(primary_key=True)
    sale_date = models.DateField()
    stock_ref = models.ForeignKey(Stock, on_delete=models.CASCADE)
    amount = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sales'

def __str__(self):
        return "{} {} {}".format(self.sale_date, self.stock_ref, self.amount)
