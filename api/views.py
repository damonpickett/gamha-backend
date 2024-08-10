from rest_framework import viewsets
from .models import Post, Book
from .serializers import PostSerializer, BookSerializer
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse

def upload_test_file(request):
    file_name = "test_file.txt"
    file_content = "This is a test file content"  # Example content

    # Convert string content to bytes
    file_content_bytes = file_content.encode('utf-8')

    # Save the file
    file_path = default_storage.save(file_name, ContentFile(file_content_bytes))

    return HttpResponse(f"File uploaded to {file_path}")

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('order')
    serializer_class = BookSerializer

def home(request):
    return HttpResponse("Welcome to the Home Page")