from rest_framework import routers
from .views import AssignmentViewList

router = routers.DefaultRouter()
router.register("", AssignmentViewList, basename="assignments")
urlpatterns = router.urls
