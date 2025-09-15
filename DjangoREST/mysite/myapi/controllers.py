from rest_framework import status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from drf_spectacular.types import OpenApiTypes
from .models import Hero
from .serializers import HeroSerializer


class HeroController:
    """Controller для операций с героями"""

    @staticmethod
    @extend_schema(
        summary='Получить всех героев',
        description='Возвращает список всех героев отсортированных по имени',
        responses={200: HeroSerializer(many=True)}
    )
    def get_all_heroes():
        """Получить всех героев"""
        heroes = Hero.objects.all().order_by('name')
        return HeroSerializer(heroes, many=True)

    @staticmethod
    @extend_schema(
        summary='Получить героя по ID',
        description='Находит героя по ID',
        responses={
            200: HeroSerializer,
            404: OpenApiTypes.OBJECT
        }
    )
    def get_hero_by_id(hero_id):
        """Получить героя по ID"""

        try:
            # Преобразуем id в int, так как из URL он приходит как строка
            hero = HeroController.get_hero_by_id(hero_id)
            return hero
        except Hero.DoesNotExist:
            return Response(
                {'error': f'Hero with id "{hero_id}" not found'},
                status=status.HTTP_404_NOT_FOUND
            )
