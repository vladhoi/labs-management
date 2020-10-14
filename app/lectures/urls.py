from django.urls import path

from .views import LectureView

urlpatterns = [
    path("lecture/<int:pk>", LectureView.as_view())
]
