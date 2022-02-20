from rest_framework import serializers

from table_game.models import Personage, CardSpell, CardTreasure, CardDeath


class PersonageSer(serializers.ModelSerializer):
	class Meta:
		model = Personage
		fields = '__all__'


class CardSpellSer(serializers.ModelSerializer):
	class Meta:
		model = CardSpell
		fields = '__all__'


class CardDeathSer(serializers.ModelSerializer):
	class Meta:
		model = CardDeath
		fields = '__all__'


class CardTreasureSer(serializers.ModelSerializer):
	class Meta:
		model = CardTreasure
		fields = '__all__'
