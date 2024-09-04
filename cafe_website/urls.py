from django.contrib import admin
from django.urls import path, include
from cafe.urls import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("cafe.urls")),
    # path('members/', views.member_list, name='member_list'),
]
