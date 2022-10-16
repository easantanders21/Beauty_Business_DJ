from django.urls import path
from . import views


app_name = "management"
urlpatterns = [
    path("", views.index, name="index"),
    path("sales_record/", views.sales_record, name="sales_record"),
    path("purchases/", views.purchases, name="purchases"),
    path("confirmation/", views.confirmation, name="confirmation"),
    path("error_handling/", views.error_handling, name="error_handling")
]
