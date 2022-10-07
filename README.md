# Beauty_Business_DJ
Beauty_Business_DJ

Tareas:

Limitar las ventas a la cantidad de producto disponible
todo por id
agregarlo al formulario para ver la limitante de cantidad de producto

Agregar a la base de datos precio de venta en sales.
Total en la factura en stock
agregar el nombre al diccionario

dbdiagram.io


products_available = (Stock.objects.values('product_id_id').annotate(total=Sum('amount'), price=Max('sales_price')).order_by())
    print(Stock.objects.filter(amount__gt = 0).values('product_id_id').annotate(total=Sum('amount'), price=Max('sales_price')).order_by().query)