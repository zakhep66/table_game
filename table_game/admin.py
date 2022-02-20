from django.contrib import admin

from .models import CardSpell, Personage, CardDeath, CardTreasure

admin.site.register(CardSpell)
admin.site.register(Personage)
admin.site.register(CardDeath)
admin.site.register(CardTreasure)
