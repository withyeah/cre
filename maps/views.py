from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DongSerializer
from .models import City, Gu, Dong
from IPython import embed

# Create your views here.

@api_view(['GET'])
def region_detail(request, region_name):
    region = Dong.objects.filter(
        Q(city_name=region_name) | Q(city_name_en=region_name) |
        Q(gu_name=region_name) | Q(gu_name_en=region_name) |
        Q(dong_name=region_name) | Q(dong_name_en=region_name)
    )
    serializer = DongSerializer(region, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def father(request, region_code):
    if len(str(region_code)) == 4:
        result = [City.objects.get(city_code=region_code).country_name]
    elif len(str(region_code)) == 7:
        region = Gu.objects.get(gu_code=region_code)
        result = [region.country_name, region.city_name]
    else:
        region = Dong.objects.get(dong_code=region_code)
        result = [region.country_name, region.city_name, region.gu_name]
    return JsonResponse({
        'region_code' : region_code,
        'parent_regions' : result,
    })