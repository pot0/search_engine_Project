# Create your views here.
#view.py
from django.shortcuts import render
from rest_framework.response import Response
from ..product.models import Product
from rest_framework.views import APIView
from ..product.serializers import ProductSerializer

class ProductListAPI(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        print(queryset)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)