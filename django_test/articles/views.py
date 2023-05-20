from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticlesForm
from datetime import datetime
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        article = Article.objects.all().order_by('-created')
        return render(request, 'articles/articles.html', {'articles' : article})

    
class OneArticleView(View):
    def get(self, request, *args, **kwargs):
        id_article = kwargs.get('id')
        article = get_object_or_404(Article, id=id_article)
        return render(request, 'articles/one_article.html', {'article' : article})
    

class ArticleCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticlesForm()
        return render(request, 'articles/create.html', {'form' : form})
    
    def post(self, request, *args, **kwargs):
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(request, 'articles/create.html', {'form': form})
    

class ArticleUpdateView(View):
    def get(self, request, *args, **kwargs):
        id_article = kwargs.get('id')
        article = Article.objects.get(id=id_article)
        form = ArticlesForm(instance=article)
        return render(request, 'articles/update.html', {'form' : form})
    
    def post(self, request, *args, **kwargs):
        id_article = kwargs.get('id')
        article = Article.objects.get(id=id_article)
        form = ArticlesForm(request.POST, instance=article)
        if form.is_valid():
            article_mod = form.save(commit=False)
            article_mod.modified = datetime.now()
            article_mod.save()
            return redirect('articles')
        return render(request, 'articles/update.html', {'form': form})
    

class ArticleDeleteView(View): 
    def get(self, request, *args, **kwargs):
        return render(request, 'articles/delete.html')


    def post(self, request, *args, **kwargs):
        id_article = kwargs.get('id')
        article = Article.objects.get(id=id_article)
        if article:
            article.delete()
            return redirect('articles')