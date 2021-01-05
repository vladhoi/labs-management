from rest_framework import routers
from .views import (
    AssignmentViewList,
    UserAssignmentsViewList,
    AssignmentSubmissionsViewList,
)
from django.urls import path

router = routers.DefaultRouter()
router.register("", AssignmentViewList, basename="assignments")

urlpatterns = [
    path(
        "user/<int:id>/",
        UserAssignmentsViewList.as_view(),
        name="user-assignments",
    ),
    path(
        "<int:id>/submissions",
        AssignmentSubmissionsViewList.as_view(),
        name="assignment-submissions",
    ),
]
urlpatterns += router.urls
