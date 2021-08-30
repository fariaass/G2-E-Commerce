from account.views import cadastra_user
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . import settings
from carrinho.api.viewsets import CarrinhoViewSet
from produtos.api.viewsets import ProdutoViewSet
from account.api.viewsets import MyUserViewSet
from categorias.api.viewsets import CategoriaViewSet, TagViewSet
from .views import home
from produtos.views import retorna_produtos_mais_vendidos, retorna_produtos_mais_visualizados

router = DefaultRouter()
router.register(r'account', MyUserViewSet, basename='account')
router.register(r'produtos', ProdutoViewSet, basename='produtos')
router.register(r'carrinho', CarrinhoViewSet, basename='carrinho')
router.register(r'categorias', CategoriaViewSet, basename='categorias')
router.register(r'tags', TagViewSet, basename='tags')

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastrar/', cadastra_user, name='cadastrar'),
    path('maisVisitados/', retorna_produtos_mais_visualizados, name='maisVisitados'),
    path('maisVendidos/', retorna_produtos_mais_vendidos, name='maisVendidos'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
