from django.urls import path
from rest_framework import routers

from .views import LectureViewList, LectureView

"""
Django REST url
"""

router = routers.DefaultRouter()
router.register("", LectureViewList, basename="lectures")
urlpatterns = [path("new/", LectureView.as_view())]

urlpatterns += router.urls
