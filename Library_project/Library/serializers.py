from rest_framework import serializers
from .models import Book, Author, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'birth_date']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'address', 'website']


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    publisher = PublisherSerializer(read_only=True)

    author_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Author.objects.all(),
        source='authors',
        write_only=True
    )
    publisher_id = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(),
        source='publisher',
        write_only=True
    )

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'isbn', 'publication_date',
            'authors', 'publisher', 'author_ids', 'publisher_id'
        ]