from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count, Sum, Max
from django.db import connection

from .models import Stock, Category, Products, Sales


def index(request):
    products_available = Stock.objects.raw(
        '''SELECT 1 AS stock_id, s.product_id_id,
            sum(s.amount) AS total,
            MAX(s.sales_price) AS price,
            p.name_product AS nombre 
        FROM stock AS s 
        INNER JOIN products AS p ON s.product_id_id = p.product_id 
        WHERE s.amount > 0 
        GROUP BY s.product_id_id, p.name_product ORDER BY s.product_id_id'''
    )
    latest_Products = Products.objects.all()
    return render(request, "management/index.html", {
        "latest_Products": latest_Products,
        "products_available": products_available
    })

def sales_record(request):
    """ primero verificamos si es un metodo post """
    print(request)
    if request.method == "POST":
        """ obtenemos el id del producto vendido, la cantidad casteados como enteros y el precio """
        try:
            sold_product_id = int(request.POST.get("product_sale"))
            amount = int(request.POST.get("amount"))
            price = int(request.POST.get("price"))
        except ValueError:
            print("Value Error")
            response = redirect('/management/')
            return response
    else:
        response = redirect('/management/')
        return response

    """ ahora buscamos el producto en el inventario 'stock' para descontar los vendido """
    product_in_stock = Stock.objects.filter(product_id_id = sold_product_id, amount__gt = 0).values()
    """ si encontramos existencias hacemos el descuento """

    if len(product_in_stock) == 0:
        print("No hay unidades disponibles de ese producto")
        response = redirect('/management/')
        return response
    else:
        """ ojo que tenemos es un diccionario entonces tenemos que traer la row (instancia) para descontar
        ojo primero necesitamos el id en stock para eso """
        stock_id = product_in_stock[0]["stock_id"]
        stock_discharge = get_object_or_404(Stock, pk = stock_id)
        print("id stock: {} -- id producto: {} -- cantidad disp {} ".format(stock_id, sold_product_id, stock_discharge.amount))
        if amount <= stock_discharge.amount:
            stock_discharge.amount -= amount
            stock_discharge.sales_st += amount
            try:
                stock_discharge.save()
                print("se realizo la desgarga exitosamente")
            except:
                print("no se pudo hacer la descarga")
        else: 
            print("no hay suficiente producto para realizar la venta")
            response = redirect('/management/')
            return response

    """ tambien es importante traernos el objeto producto para registrar la venta """
    sold_product = get_object_or_404(Products, pk = sold_product_id)

    """ por ultimo registramos la venta """
    """ por ahora vamos a crear el ultimo registro recuperando el ultimo pk """
    last_sale = Sales.objects.all().last()
    last_sale_id = last_sale.sale_id + 1
    print("este es el nuevo registro {}".format(last_sale_id))
    sale = Sales(sale_id = last_sale_id, stock_id = stock_discharge, product_id = sold_product, amount = amount, price = price)
    sale.save()
    print("venta finalizada con exito: {}".format(sale))
    
    response = redirect('/management/confirmation')
    return response

#    latest_Products = Products.objects.all()
#    return render(request, "management/index.html", {
#        "latest_Products": latest_Products,
#        "Bandera": "true"
#    })

def confirmation(request):
    return render(request, "management/confirmation.html", {
    })
