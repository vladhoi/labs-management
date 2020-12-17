"""users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    UserList,
    UserProfileView,
    UserProfileList,
    GroupUserListView,
    UserGroupList,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("", UserList, basename="user-list"),

urlpatterns = [
    path("<int:pk>/profile/", UserProfileView.as_view(), name="user-profile"),
    path("profiles/", UserProfileList.as_view(), name="user-profiles"),
    path("group/<str:group>/", GroupUserListView.as_view(), name="user-group-profiles"),
    path("groups/", UserGroupList.as_view(), name="user-groups"),
]
urlpatterns += router.urls
