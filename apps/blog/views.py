from django.shortcuts import render
from django.urls import reverse

from apps.blog.forms import CommentForm
from apps.blog.models import BlogCategory, Article, Tag, Comments


def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    breadcrumbs = {'current': 'Блог'}
    return render(request, 'blog/category_list.html', {"categories": blog_categories, 'breadcrumbs': breadcrumbs})

def article_list(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    category = BlogCategory.objects.get(id=category_id)
    breadcrumbs = {reverse('blog_category_list'): 'Блог', 'current': category.name}
    return render(request, 'blog/article_list.html', {
        'articles': articles,
        'category': category,
        'breadcrumbs': breadcrumbs,
    })

def article_view(request, category_id, article_id):
    category = BlogCategory.objects.get(id=category_id)
    article = Article.objects.get(id=article_id)
    breadcrumbs = {reverse('blog_category_list'): 'Блог', reverse('blog_article_list', kwargs={'category_id': category.id}): category.name, 'current': article.title}

    return render(request, 'blog/article_view.html', {'category': category, 'article': article, 'breadcrumbs': breadcrumbs})


def tag_search_view(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    articles = Article.objects.filter(tags=tag)
    return render(request, 'blog/tag_search.html', {'tag': tag, 'articles': articles})


def comment_view(request, article_id):
    comments = Comments.objects.get(is_active=True)
    print(comments)
    if request.user.is_authenticated:
        # new_comment = CommentForm.save()

        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return render(request, 'blog/article_view.html', {'comments': comments})

    return render(request, 'blog/article_view.html', {})
