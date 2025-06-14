from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer 
from .permissions import IsOwnerOrReadOnly
class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]  

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated] 

class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]  

class PostUpdateAPIView(generics.UpdateAPIView):  
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]

class PostDestroyAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwnerOrReadOnly]  

class MyPostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]  
    
    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user) 
    


# views.py
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .telegram_bot import TelegramBot

@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        update = json.loads(request.body)
        bot = TelegramBot()
        bot.handle_update(update)
        return JsonResponse({'ok': True})
    return JsonResponse({'error': 'Method not allowed'}, status=405)