from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .models import Item
from .serializers import ItemSerializer

# Create your views here.
class ItemListAPI(APIView):
  def get(self, request):
    queryset=Item.objects.all()
    print(queryset)
    serializer=ItemSerializer(queryset, many=True)
    return Response(serializer.data)