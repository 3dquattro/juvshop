from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import (
    JewelrySerializer,
    MaterialSerializer,
    ProductTypeSerializer,
    PartTypeSerializer,
    PartSerializer,
    PartSmallSerializer,
)
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from core.models import Material, ProductType, PartType, Part, Jewelry
import logging
from rest_framework.parsers import JSONParser
from rest_framework import status
import json
import base64
from django.core.files.base import ContentFile


# API for materials list
@api_view(["GET"])
def api_materials_list(request):
    if request.method == "GET":
        material = Material.objects.all()
        serializer = MaterialSerializer(material, many=True)
        return JsonResponse(serializer.data, safe=False)


# GET for list of products type list
@api_view(["GET"])
def api_product_type_list(request):
    if request.method == "GET":
        product_type = ProductType.objects.all()
        serializer = ProductTypeSerializer(product_type, many=True)
        return JsonResponse(serializer.data, safe=False)


# GET for constructor, list of part types for product type
@api_view(["GET"])
def api_part_types_for_product(request, producttype):
    # GET для передачи в конструктор
    if request.method == "GET":
        part_types = PartType.objects.filter(productType__id=producttype).order_by("id")
        return JsonResponse(PartTypeSerializer(part_types, many=True).data, safe=False)


# GET for jewelry
@api_view(["GET", "POST", "PUT"])
@permission_classes((IsAuthenticated,))
def api_jewelry(request, id=0):
    if request.method == "GET":
        jewelry = Jewelry.objects.get(pk=id)
        if request.user.is_authenticated is False or jewelry.user_id != request.user.id:
            return None
        serializer = JewelrySerializer(jewelry)
        return JsonResponse(serializer.data, safe=False)
    # POST/PUT for insert/edit
    if request.method in ["POST", "PUT"]:
        if request.method == "POST":
            jewelry = Jewelry.objects.create(user_id=request.data["user"])
        else:
            jewelry = Jewelry.objects.get(pk=request.data["id"])
        jewelry.material_id = request.data["material"]
        jewelry.name = request.data["name"]
        jewelry.parts.set([int(x) for x in request.data["parts"]])
        image_data = request.data["preview"]
        format, imgstr = image_data.split(";base64,")
        ext = format.split("/")[-1]
        data = ContentFile(base64.b64decode(imgstr))
        file_name = "'" + str(request.data["id"]) + "-" + "prvw." + ext
        jewelry.preview.save(file_name, data, save=True)
        jewelry.save()
        return JsonResponse(request.data, status=status.HTTP_201_CREATED)


# GET for parts by category
@api_view(["GET"])
def api_parts_for_category(request, category):
    if request.method == "GET":
        parts = Part.objects.filter(category__id=category)
        return JsonResponse(PartSmallSerializer(parts, many=True).data, safe=False)


# GET for parts categories as object
@api_view(["GET"])
def api_partts_as_object(request, producttype):
    if request.method == "GET":
        parttypes = PartType.objects.filter(productType__id=producttype).only(
            "id", "name"
        )
        return JsonResponse(PartSmallSerializer(parttypes, many=True).data, safe=False)


# GET for single part for constructor
@api_view(["GET"])
def api_single_part(request, sid):
    if request.method == "GET":
        part = Part.objects.get(id=sid)
        return JsonResponse(PartSerializer(part).data, safe=False)
