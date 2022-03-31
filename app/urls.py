from app.views import (RegionGetOrPost, RegionDeleteOrPut,
        FruitsGetOrPost, FruitsDeleteOrPut)

from django.urls import path

urlpatterns = [
        path('region/', RegionGetOrPost.as_view()),
        # operando em um único objeto
        path('region/<int:pk>/', RegionDeleteOrPut().as_view()),

        path('fruits/', FruitsGetOrPost.as_view()),
        path('fruits/<int:pk>/', FruitsDeleteOrPut().as_view()),
]
