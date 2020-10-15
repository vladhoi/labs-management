from django.urls import path

from .views import LectureView

"""
Django REST url
"""
urlpatterns = [path("lecture/<int:pk>", LectureView.as_view())]
