from rest_framework.routers import DefaultRouter
from apps.api.blog.views import ArticleViewSet, ArticleImageViewSet

urlpatterns = []

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('article/image', ArticleImageViewSet, basename='article_image')

urlpatterns += router.urls
