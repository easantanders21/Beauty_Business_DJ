from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Count, Sum, Max
from django.db import connection

from .models import Stock, Category, Products, Sales, Mark, Providers


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

    """ Vamos a validar si hay unidades suficientes para efectuar la venta """
    sales_units = Stock.objects.filter(product_id_id = sold_product_id, amount__gt = 0).aggregate(total = Sum('amount'))


    if sales_units['total'] == None:
        return render(request, "management/error_handling.html", {
            "error": "No hay existencias en stock",
        })
    elif sales_units['total'] < amount:
        return render(request, "management/error_handling.html", {
            "error": "No existen suficientes unidades para realizar la venta",
        })

    """ ahora buscamos los lotes de producto en el inventario 'stock' para descontar los vendido """
    product_in_stock = Stock.objects.filter(product_id_id = sold_product_id, amount__gt = 0).values()

    if product_in_stock:
        for i in product_in_stock:
            if amount > 0:
                stock_id = i['stock_id']
                stock_discharge = get_object_or_404(Stock, pk = stock_id)
                if amount >= i['amount']:
                    stock_discharge.deduct_in_stock(i['amount'])
                    last_sale = Sales.objects.all().last()
                    last_sale_id = last_sale.sale_id + 1
                    sold_product = get_object_or_404(Products, pk = sold_product_id)
                    sale = Sales(sale_id = last_sale_id, stock_id = stock_discharge, product_id = sold_product, amount = i['amount'], price = price)
                    sale.save()
                    amount -= i['amount']
                elif amount < i['amount']:
                    stock_discharge.deduct_in_stock(amount)
                    last_sale = Sales.objects.all().last()
                    last_sale_id = last_sale.sale_id + 1
                    sold_product = get_object_or_404(Products, pk = sold_product_id)
                    sale = Sales(sale_id = last_sale_id, stock_id = stock_discharge, product_id = sold_product, amount = amount, price = price)
                    sale.save()
                    amount -= amount
                elif amount == 0:
                    break                    
        response = redirect('/management/confirmation')
        return response

    response = redirect('/management/confirmation')
    return response


def purchases(request):
    return render(request, "management/purchases.html", {
    })


def mark_register(request):
    if request.method == "POST":
        """ obtenemos el id del producto vendido, la cantidad casteados como enteros y el precio """
        try:
            mark_name = request.POST.get("new_mark")
        except ValueError:
            print("Value Error")
    else:
        return render(request, "management/error_handling.html", {
        })

    last_mark = Mark.objects.all().last()
    last_mark_id = last_mark.mark_id + 1
    new_mark = Mark(mark_id = last_mark_id, name_mark = mark_name)
    new_mark.save()
    
    if isinstance(new_mark, Mark):
        response = redirect('/management/confirmation')
        return response
    else:
        return render(request, "management/error_handling.html", {
    })


def category_register(request):
    if request.method == "POST":
        """ obtenemos el id del producto vendido, la cantidad casteados como enteros y el precio """
        try:
            category_name = request.POST.get("new_category")
        except ValueError:
            print("Value Error")
    else:
        return render(request, "management/error_handling.html", {
        })

    last_category = Category.objects.all().last()
    last_category_id = last_category.category_id + 1
    new_category = Category(category_id = last_category_id, name_category = category_name)
    print(new_category.name_category)
    new_category.save()
    
    if isinstance(new_category, Category):
        response = redirect('/management/confirmation')
        return response
    else:
        return render(request, "management/error_handling.html", {
    })


def provider_register(request):
    if request.method == "POST":
        """ obtenemos el id del producto vendido, la cantidad casteados como enteros y el precio """
        try:
            provider_name = request.POST.get("name_provider")
            phone = request.POST.get("phone")
            addres = request.POST.get("addres")
        except ValueError:
            print("Value Error")
    else:
        return render(request, "management/error_handling.html", {
        })

    last_provider = Providers.objects.all().last()
    last_provider_id = last_provider.provider_id + 1
    new_provider = Providers(provider_id = last_provider_id, provider_name = provider_name, phone = phone, provider_address = addres)
    new_provider.save()
    
    if isinstance(new_provider, Providers):
        response = redirect('/management/confirmation')
        return response
    else:
        return render(request, "management/error_handling.html", {
    })


def confirmation(request):
    return render(request, "management/confirmation.html", {
    })


def error_handling(request):
    return render(request, "management/error_handling.html", {
    })
