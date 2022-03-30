from app.models import Region, Fruits
from app.serializers import RegionSerializer, FruitsSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def RegionList(request):
    # pegando todas as regiões do br
    regions = Region.object.all()

    serializer = RegionSerializer(regions, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def FruitsList(request):
    # pegando todos os (as) objetos (frutas) do db
    fruits = Fruits.objects.all()

    serializer = FruitsSerializer(fruits, many=True)

    return Response(serializer.data)
