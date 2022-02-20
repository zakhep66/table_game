from rest_framework import viewsets, permissions

from table_game.models import Personage, CardSpell, CardDeath, CardTreasure
from table_game.serializers import PersonageSer, CardSpellSer, CardTreasureSer, CardDeathSer


class PersonageViewSet(viewsets.ModelViewSet):
	queryset = Personage.objects.all()
	permissions_classes = [
		permissions.AllowAny
	]
	serializer_class = PersonageSer


class CardSpellViewSet(viewsets.ModelViewSet):
	queryset = CardSpell.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = CardSpellSer


class CardTreasureViewSet(viewsets.ModelViewSet):
	queryset = CardTreasure.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = CardTreasureSer


class CardDeathViewSet(viewsets.ModelViewSet):
	queryset = CardDeath.objects.all()
	permission_classes = [
		permissions.AllowAny
	]
	serializer_class = CardDeathSer
