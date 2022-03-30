from app.views import RegionList

from django.urls import path

urlpatterns = [
        path('', RegionList),
]
