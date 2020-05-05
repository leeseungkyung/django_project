from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm, CommentForm
# Create your views here.

def index(request):

    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method=='POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            print("통과")
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form':form
    }

    return render(request, 'articles/form.html', context)