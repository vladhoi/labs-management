from rest_framework import routers
from .views import AssignmentViewList, UserAssignmentsViewList
from django.urls import path

router = routers.DefaultRouter()
router.register("", AssignmentViewList, basename="assignments")

urlpatterns = [
    path(
        "user/<int:id>/",
        UserAssignmentsViewList.as_view(),
        name="user-assignments",
    ),
]
urlpatterns += router.urls
