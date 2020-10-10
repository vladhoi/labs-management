from users.views import UserList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserList)