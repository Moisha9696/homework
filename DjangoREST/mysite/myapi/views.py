
from .serializers import HeroSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.decorators import action

from .models import Hero

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

class HeroViewSet(viewsets.ViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

    def get_serializer(self, *args, **kwargs):
        return HeroSerializer(*args, **kwargs)

    @extend_schema(
        summary='Получить всех героев',
        description='Возвращает список всех героев отсортированных по имени',
        responses={200: HeroSerializer(many=True)}
    )
    @action(detail=False, methods=['get'], url_path='all')
    def get_all(self, request):
        """Получить всех героев"""
        # heroes = self.get_queryset()
        heroes = Hero.objects.all()
        serializer = self.get_serializer(heroes, many=True)
        return Response(serializer.data)


    @extend_schema(
        summary='Получить героя по ID',
        description='Находит героя по ID',
        responses={
            200: HeroSerializer,
            404: OpenApiTypes.OBJECT
        }
    )
    @action(detail=False, methods=['get'], url_path='get/(?P<id>\d+)')
    def get_by_id(self, request, id=None):
        """Получить героя по ID"""
        try:
            # Преобразуем id в int, так как из URL он приходит как строка
            hero_id = int(id)
            hero = Hero.objects.get(id=hero_id)
            serializer = self.get_serializer(hero)
            return Response(serializer.data)
        except Hero.DoesNotExist:
            return Response(
                {'error': f'Hero with id "{id}" not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        except (ValueError, TypeError):
            return Response(
                {'error': 'ID must be a valid integer'},
                status=status.HTTP_400_BAD_REQUEST
            )

class HelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello, {request.user.username}!"})
from django.shortcuts import render

# Create your views here.
