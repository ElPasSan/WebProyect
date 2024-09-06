from django.shortcuts import render
from .models import Post

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'post_list.html', {'posts': posts})

def home(request):
    return render(request, 'home.html')

def sobre_nosotros(request):
      return render(request, 'sobre_nosotros.html')
# Create your views here.
