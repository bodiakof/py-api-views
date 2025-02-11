from rest_framework import status, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from cinema.models import Actor, Genre, CinemaHall, Movie
from cinema.serializers import (
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSerializer
)


class ActorList(GenericAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request: Request, *args, **kwargs) ->Response:
        actors = self.get_queryset()
        serializer = self.get_serializer(actors, many=True)
        return Response(serializer.data)

    def post(self, request: Request, *args, **kwargs) ->Response:
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActorDetail(GenericAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get(self, request: Request, *args, **kwargs) ->Response:
        actor = self.get_object()
        serializer = self.get_serializer(actor)
        return Response(serializer.data)

    def put(self, request: Request, *args, **kwargs) ->Response:
        actor = self.get_object()
        serializer = self.get_serializer(actor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, *args, **kwargs) ->Response:
        actor = self.get_object()
        serializer = self.get_serializer(actor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, *args, **kwargs) ->Response:
        actor = self.get_object()
        actor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenreList(APIView):
    def get(self, request: Request, *args, **kwargs) ->Response:
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request: Request, *args, **kwargs) ->Response:
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetail(APIView):
    def get(self, request: Request, pk: int, *args, **kwargs) -> Response:
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def put(self, request: Request, pk: int, *args, **kwargs) -> Response:
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, pk: int, *args, **kwargs) -> Response:
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int, *args, **kwargs) -> Response:
        genre = Genre.objects.get(pk=pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CinemaHallViewSet(GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
