from rest_framework import routers

from table_game.views import PersonageViewSet, CardSpellViewSet, CardDeathViewSet, CardTreasureViewSet

router = routers.DefaultRouter()


router.register('api/personage', PersonageViewSet, 'personage')
router.register('api/card-spell', CardSpellViewSet, 'card_spell')
router.register('api/card-death', CardDeathViewSet, 'card_death')
router.register('api/card-treasure', CardTreasureViewSet, 'card_treasure')

urlpatterns = router.urls
