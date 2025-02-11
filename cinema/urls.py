from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreDetail,
    GenreList,
    ActorDetail,
    ActorList,
    CinemaHallViewSet,
    MovieViewSet, GenreList, GenreDetail, ActorList, ActorDetail
)


router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"cinema_halls", CinemaHallViewSet, basename="cinema_hall")

urlpatterns = [
    path("cinema/genres/", GenreList.as_view(), name="genre-list-create"),
    path("cinema/genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),

    # Actor URLs using ActorGenericAPIView
    path("cinema/actors/", ActorList.as_view(), name="actor-list-create"),
    path("cinema/actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("", include(router.urls)),
]

app_name = "cinema"
