from django.urls import path
from . import views
from rest_framework import routers
from .views import LectureView

urlpatterns = [
    path("lecture/<int:pk>", LectureView.as_view())
]