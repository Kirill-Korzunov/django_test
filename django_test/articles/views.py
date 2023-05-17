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
            article = Article(
                title=form['title'].value(),
                text=form['text'].value(),
                created=datetime.now(),
                modified=datetime.now(),
                )
            article.save()
            return redirect('articles')
        return render(request, 'articles/create.html', {'form': form})
    

