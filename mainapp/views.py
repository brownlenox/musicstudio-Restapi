from django.shortcuts import render, HttpResponse
from mainapp.models import Artist, Song
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mainapp import serializers

# Create your views here.
def home(request):
    # artist = Artist.objects.order_by("?").first()
    # print(artist)
    # albums = artist.album_set.all()
    # print(albums)
    # for alb in albums:
    #     print(alb.name, alb.release_year)
    #     songs = alb.songs.all()
    #     print("Songs are ", songs)
    #     for s in songs:
    #         print("Song -", s.title, s.duration, "seconds")

    song = Song.objects.order_by("?").first()
    print(song)
    album = song.album
    artists = song.album.artists.all().values("name")
    print("artists")

    # song.album.artists.all()

    return HttpResponse("Check results on the console")

    # TODO 

@api_view
def save_or_fetch_artists(request):
    if requrest.method == "GET":
        artist=Artist.objects.all()
        serializer=ArtistSerializer(instanxe=artist, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"message":"Succesfully deleted", "data":serializer.data})

@api_view(["GET"])
def fetch_one_artist(request, id):
    try:
        artist = Artist.objects.get(pk=id)
        serializer = ArtistSerializer(instance=Artist)
        return Response(serializer.data)
    except:
        return Response({"error":"Artist not found"}, status=404)

@api_view(["PUT", "PATCH"])
def update_artist(request):
    try:
        artist = Artist.objects.get(pk=id)
        serializer = ArtistSerializer(instance=artist, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    except:
        return Response({"error":"Artist not found"}, status=404)

@api_view(["DELETE"])
def delete_artist(request):
    try:
        artist = Artist.objects.get(pk=id)
        serializer = ArtistSerializer(instance=artist, data=request.data)
        return Response({"message":"Succesfully deleted"})
    except:
        return Response({"error":"Artist not found"}, status=404)

@api_view(["GET"])
def album_for_artist(request, id):
    try:
        artist = Artist.objects.get(pk=id)
        serializer = ArtistAlbumSerializer(instance=artist, data=request.data)
        return Response(serializer.data)
    except:
        return Response({"error":"Artist not found"}, status=404)


