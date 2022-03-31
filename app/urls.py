from app.views import (RegionGetOrPost, RegionDeleteOrPut,
        FruitsGetOrPost)

from django.urls import path

urlpatterns = [
        path('region/', RegionGetOrPost.as_view()),
        # operando em um único objeto
        path('<int:pk>/', RegionDeleteOrPut().as_view()),

        path('fruits/', FruitsGetOrPost.as_view()),
]
