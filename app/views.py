from app.models import Region, Fruits
from app.serializers import RegionSerializer, FruitsSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

@api_view(['GET', 'POST'])
def RegionList(request):

    if request.method == 'GET':
        # pegando todas as regiões do br
        regions = Region.objects.all()

        serializer = RegionSerializer(regions, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RegionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # caso a requisição tenha sido feita incorretamente
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def FruitsList(request):
    # pegando todos os (as) objetos (frutas) do db
    fruits = Fruits.objects.all()

    serializer = FruitsSerializer(fruits, many=True)

    return Response(serializer.data)
