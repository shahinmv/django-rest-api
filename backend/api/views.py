#from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

import json

from products.models import Product
from products.serializers import ProductSerializer
from django.forms.models import model_to_dict


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """ serializer = ProductSerializer(data=request.data)
    print(request.data)
    print(serializer)
    if serializer.is_valid():
        print("test true")
        print(serializer.data)
        data = serializer.data 
        return Response(data) """
    
    data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        print('serializer is valid')
        instance = serializer.save()
        print(instance)
    print('serializer is not valid')
    return Response(serializer.data)
