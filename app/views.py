from app.models import Region, Fruits
from app.serializers import RegionSerializer, FruitsSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

from rest_framework import status

class RegionGetOrPost(APIView):

    def get(self, request):
        # pegando todas as regiões do br
        regions = Region.objects.all()

        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # caso a requisição tenha sido feita incorretamente
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegionDeleteOrPut(APIView):

    def get_object(self, pk):
        try:
            return Region.objects.get(pk=pk)

        except Region.DoesNotExists:
            raise NotFound()

    def get(self, request, pk):
        regions = self.get_object(pk)

        serializer = RegionSerializer(regions)
        return Response(serializer.data)

    def put(self, request, pk):
        regions = self.get_object(pk)

        serializer = RegionSerializer(regions, data=request.data)

        if serializer.is_valid():
            serializer.save()
            #status == 200 no método post por padrão
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        regions = self.get_object(pk)

        regions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FruitsGetOrPost(APIView):

    def get(self, request):
        # pegando todos os (as) objetos (frutas) do db
        fruits = Fruits.objects.all()

        serializer = FruitsSerializer(fruits, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = FruitsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FruitsDeleteOrPut(APIView):
    def get_object(self, pk):
        try:
            return Fruits.objects.get(pk=pk)

        except Fruits.DoesNotExists:
            raise NotFound()

    def get(self, request, pk):
        fruit = self.get_object(pk)

        serializer = RegionSerializer(fruit)
        return Response(serializer.data)

    def put(self, request, pk):
        fruit = self.get_object(pk)

        serializer = RegionSerializer(fruit, data=request.data)

        if serializer.is_valid():
            serializer.save()
            #status == 200 no método post por padrão
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        fruit = self.get_object(pk)

        fruit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
