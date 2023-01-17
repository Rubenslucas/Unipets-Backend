from rest_framework import routers
from users.views import UserViewSet
from pets.views import PetViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'users', UserViewSet, basename='users')
router.register(r'pets', PetViewSet, basename='pets')