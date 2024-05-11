from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter().order_by('-created_date')
    return render(request, 'list/post_list.html', {'posts': posts})

def about(request) :
    return render(request, 'list/post_list.html')