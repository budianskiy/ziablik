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
    comments = Comments.objects.filter(article=article, is_checked=True).reverse()
    return render(request, 'blog/article_view.html', {'category': category, 'article': article, 'breadcrumbs': breadcrumbs, 'comments': comments})


def tag_search_view(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    articles = Article.objects.filter(tags=tag)
    return render(request, 'blog/tag_search.html', {'tag': tag, 'articles': articles})


def create_comment(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        data = request.POST.copy()
        data.update(article=article_id)

        if not request.user.is_anonymous:
            user = request.user
            data.update({
                "name": f"{user.last_name} {user.first_name}",
                "is_checked": True,
                "email": user.email,
                "user": user
            })

        request.POST = data
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            breadcrumbs = {'current': 'Комментарий успешно добавлен'}
            return render(request, 'blog/comment_created.html', {
                "comment": comment,
                "breadcrumbs": breadcrumbs,
                "article": article
            })