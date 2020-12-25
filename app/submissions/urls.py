from rest_framework import routers
from .views import SubmissionViewList, FileDownloadListAPIView
from django.urls import path

router = routers.DefaultRouter()
router.register("", SubmissionViewList, basename="submissions")
urlpatterns = [
    path(
        "file/<str:filename>/",
        FileDownloadListAPIView.as_view(),
        name="submission-file",
    ),
]
urlpatterns += router.urls
