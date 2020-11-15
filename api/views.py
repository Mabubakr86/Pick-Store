from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from store.models import Product
from .serlizers import ProductSerlizer
from rest_framework.decorators import api_view


@api_view(['GET'])
def productslistapi(request):
    qs = Product.objects.all()
    ser = ProductSerlizer(qs, many=True)
    return Response(ser.data)


@api_view(['GET'])
def productdetailapi(request, id):
    qs = Product.objects.get(id=id)
    ser = ProductSerlizer(qs)
    return Response(ser.data)


@api_view(['POST'])
def productcreateapi(request):
    ser = ProductSerlizer(data=request.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data) 


@api_view(['POST'])
def productupdateapi(request,id):
    product = Product.objects.get(id=id)
    ser = ProductSerlizer(instance=product,data=request.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)       

@api_view(['DELETE'])
def productdeleteapi(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return Response(ser.data)   


# class ProductListApi(APIView):
#     def get(self,request,*args,**kwargs):
#         qs = Product.objects.all()
#         ser = ProductSerlizer(qs, many=True)
#         return Response(ser.data)

#     def post(self,request,*args,**kwargs):
#         ser_data = ProductSerlizer(data=request.data)
#         if ser_data.is_valid():
#             ser_data.save()
#             return Response({'success':'true'})
#         return Response(ser.errors)