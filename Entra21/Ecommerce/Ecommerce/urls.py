from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import views
from rest_framework.routers import DefaultRouter
from . import settings
from carrinho.api.viewsets import CarrinhoViewSet
from produtos.api.viewsets import ProdutoViewSet
from account.api.viewsets import MyUserViewSet
from .views import home

router = DefaultRouter()
router.register(r'account', MyUserViewSet, basename='account')
router.register(r'produtos', ProdutoViewSet, basename='produtos')
router.register(r'carrinho', CarrinhoViewSet, basename='carrinho')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', auth_views.LoginView.as_view()),
    path('home/', home, name = 'home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
