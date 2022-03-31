from app.views import RegionList, FruitsList

from django.urls import path

urlpatterns = [
        path('', RegionList),
        path('', FruitsList)
]
