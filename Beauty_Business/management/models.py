from django.db import models

# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name_category = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'category'

    def __str__(self):
        return "El nombre de la categoria es: {}".format(self.name_category)


class Mark(models.Model):
    mark_id = models.AutoField(primary_key=True)
    name_mark = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'mark'
    
    def __str__(self):
        return "El nombre de la marcaes: {}".format(self.name_mark)


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name_product = models.CharField(max_length=30)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    mark_id = models.ForeignKey(Mark, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'products'

    #def __str__(self):
    #    return "El nombre del producto es: {}".format(self.name_product)

        
class Providers(models.Model):
    provider_id = models.AutoField(primary_key=True)
    provider_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=25)
    provider_address = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'providers'

    def __str__(self):
        return "El nombre del proveedor es: {}".format(self.provider_name)


class Purchases(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    provider_id = models.ForeignKey(Providers, on_delete=models.CASCADE)
    purchase_date = models.DateField()
    factura = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'purchases'

    def __str__(self):
        return "El id de la compra es: {}".format(self.purchase_id)


class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    purchase_id = models.ForeignKey(Purchases, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    purchase_price = models.IntegerField()
    sales_price = models.IntegerField()
    amount = models.IntegerField()
    sales_st = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stock'

    def __str__(self):
        return "El id del stock es: {}".format(self.stock_id)


class Sales(models.Model):
    sale_id = models.AutoField(primary_key=True)
    sale_date = models.DateField(auto_now_add=True)
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    amount = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sales'

    def __str__(self):
        return "el id de la venta es: {}".format(self.sale_id)
