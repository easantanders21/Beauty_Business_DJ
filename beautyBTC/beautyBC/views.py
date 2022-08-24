from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from beautyBC.models import Stock
from beautyBC.serializer import StockSerializer


class beautyBC_StockAPI(APIView):

    def get(self, request):
        stock = Stock.objects.all()
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data)
