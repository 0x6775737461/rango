from app.views import RegionGetOrPost, RegionDeleteOrPut, FruitsList

from django.urls import path

urlpatterns = [
        path('', RegionGetOrPost.as_view()),
        # operando em um único objeto
        path('<int:pk>/', RegionDeleteOrPut().as_view()),

        path('', FruitsList),

]
