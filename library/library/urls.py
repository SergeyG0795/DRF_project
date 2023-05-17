from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authors.views import AuthorModelViewSet, BiographyModelViewSet, ArticleModelViewSet, BookModelViewSet

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('biographies', BiographyModelViewSet)
router.register('articles', ArticleModelViewSet)
router.register('books', BookModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
