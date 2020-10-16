from rest_framework import routers

from .views import LectureViewList

router = routers.DefaultRouter()
router.register("", LectureViewList, basename="lecture-list")
urlpatterns = router.urls
