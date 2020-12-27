from rest_framework import routers
from .views import SubmissionViewList, FileDownloadAPIView
from django.urls import path

router = routers.DefaultRouter()
router.register("", SubmissionViewList, basename="submissions")
urlpatterns = [
    path(
        "file/<str:filename>/",
        FileDownloadAPIView.as_view(),
        name="submission-file",
    ),
]
urlpatterns += router.urls
