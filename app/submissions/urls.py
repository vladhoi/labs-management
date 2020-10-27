from rest_framework import routers
from .views import SubmissionViewList

router = routers.DefaultRouter()
router.register("", SubmissionViewList, basename="submissions")
urlpatterns = router.urls
