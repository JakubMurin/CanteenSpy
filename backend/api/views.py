from django.http import JsonResponse
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import F, Q, Count

from datetime import datetime, timezone, timedelta

@api_view(['GET', 'POST'])
def canteen_list(request):
    if request.method == 'GET':
        sort = request.GET.get('sort')
        if not sort or (sort != "avg_rating" and sort != "low_price"):
            sort = "closing"
        desc = request.GET.get('desc') == "true"

        canteens = Canteen.objects.all().order_by(sort)

        current_time = datetime.now(timezone(timedelta(hours=1)))

        filter = request.GET.get('filter')
        if filter == "available_menu":
           canteens = canteens.annotate( \
                available_menu_count=Count('menu', filter=Q(menu__day=current_time.strftime("%Y-%m-%d"), menu__available__gte=F('menu__unavailable'))) \
            ).filter(available_menu_count__gt=0)
        elif filter == "vegetarian":
            canteens = canteens.annotate( \
                available_menu_count=Count('menu', filter=Q(menu__day=current_time.strftime("%Y-%m-%d"), menu__vegetarian=True)) \
            ).filter(available_menu_count__gt=0)
        elif filter == "meat":
            canteens = canteens.annotate( \
                available_menu_count=Count('menu', filter=Q(menu__day=current_time.strftime("%Y-%m-%d"), menu__meat=True)) \
            ).filter(available_menu_count__gt=0)

        if desc:
            canteens = canteens[::-1]
            
        serializer = CanteenSerializer(canteens, many=True)
        opened, closed = [], []
        for c in serializer.data:
            if c["closing"] < f"{current_time.hour}:{current_time.minute}":
                c["opened"] = False
                closed.append(c)
            else:
                c["opened"] = True
                opened.append(c)
        return JsonResponse({"canteens": opened + closed}, safe=False)

@api_view(['GET'])
def canteen_detail(request, id):
    try:
        canteen = Canteen.objects.get(pk=id)
    except Canteen.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CanteenSerializer(canteen)
        return JsonResponse(serializer.data)

@api_view(['GET'])
def menu_list(request):
    if request.method == 'GET':
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return JsonResponse({"menus": serializer.data}, safe=False)

@api_view(['GET'])   
def menu_detail(request, id):
    try:
        menu = Menu.objects.get(pk=id)
    except Menu.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MenuSerializer(menu)
        return JsonResponse(serializer.data)

@api_view(['GET'])   
def menu_by_canteen_by_date(request, canteen_id, date):
    try:
        canteen = Canteen.objects.get(pk=canteen_id)
    except Canteen.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        menu = Menu.objects.filter(canteen_id=canteen)
        if date:
            menu = menu.filter(day=date)
        serializer = MenuSerializer(menu, many=True)
        return JsonResponse(serializer.data, safe=False)
        
@api_view(['GET'])
def rating_list(request):
    if request.method == 'GET':
        menus = Rating.objects.all()
        serializer = RatingSerializer(menus, many=True)
        return JsonResponse({"ratings": serializer.data}, safe=False)
        
@api_view(['GET', 'POST'])
def ratings_by_menu(request, menu_id):
    try:
        menu = Menu.objects.get(pk=menu_id)
    except Menu.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ratings = Rating.objects.filter(menu_id=menu)
        serializer = RatingSerializer(ratings, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['PUT'])
def menu_add_available(request, menu_id):
    if request.method == 'PUT':
        menu = Menu.objects.get(pk=menu_id)
        menu.available += 1

        serializer = MenuSerializer(menu, data={"name": menu.name})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)
        
@api_view(['PUT'])
def menu_add_unavailable(request, menu_id):
    if request.method == 'PUT':
        menu = Menu.objects.get(pk=menu_id)
        menu.unavailable += 1

        serializer = MenuSerializer(menu, data={"name": menu.name})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)