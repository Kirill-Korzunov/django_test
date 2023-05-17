from django.contrib import admin
from django.urls import path, include
from articles import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='articles'),
    path('<int:id>', views.OneArticleView.as_view(), name='detail_article'),
    path('create', views.ArticleCreateView.as_view(), name='create'),
    # path('<int:id>/update', views.create, name='update'),
    # path('<int:id>/delete', views.create, name='delete'),      
]
