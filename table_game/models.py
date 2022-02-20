from django.db import models


class Personage(models.Model):
	name_personage = models.CharField(max_length=20, unique=True, verbose_name="имя персонажа")
	hp = models.IntegerField(verbose_name="количество здоровья", default=20)
	avatar = models.ImageField(verbose_name="аватар персонажа")

	class Meta:
		verbose_name = "Personage"

	def __str__(self):
		return self.name_personage


CARD_STAGE = (
	('заводила', 'заводила'),
	('новорот', 'новорот'),
	('приход', 'приход'),
)
CARD_TYPE = (
	('кумар', 'кумар'),
	('угар', 'угар'),
	('порча', 'порча'),
	('мрак', 'мрак'),
	('трава', 'трава'),
)


class Card(models.Model):
	card_spell = models.CharField(verbose_name="заклинание карты", max_length=100, unique=True)
	card_text = models.TextField(verbose_name="суть заклинания")
	card_stage = models.CharField(verbose_name="этап заклинания", choices=CARD_STAGE, max_length=20)
	card_type = models.CharField(verbose_name="тип карты", choices=CARD_TYPE, max_length=20)

	class Meta:
		verbose_name = "Card"

	def __str__(self):
		return self.card_spell
