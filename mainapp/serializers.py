from rest_framework import serializers
from . models import Artist, Song, Album

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'email', 'phone', 'id']

class AlbumSerializer(serializers.ModelSerializer):
    artists = serializers.StringRelatedField(read_only=True, many=True)
    class Meta:
        model = Artist
        fields = ['name', 'release_year', 'id', 'artists']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'duration', 'album', 'id']

class ArtistAlbumSerializer(serializers.ModelSerializer):
    # albums = serializers.StringRelatedField(read_only=True, many=True)
    albums = AlbumSerializer(read_only=True, many=True)
    class Meta:
        model = Artist
        fields = ['name', "phone", 'albums']