from Entra21.Ecommerce.produtos.views import retorna_produtos
from account.views import cadastra_user, addEndereco
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls.static import static
from . import settings
from .views import home
from produtos.views import retorna_produtos_mais_vendidos, retorna_produtos_mais_visualizados, detalhes_produto, retorna_produtos_categoria
from carrinho.views import retorna_carrinho

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastrar/', cadastra_user, name='cadastrar'),
    path('maisVisitados/', retorna_produtos_mais_visualizados, name='maisVisitados'),
    path('maisVendidos/', retorna_produtos_mais_vendidos, name='maisVendidos'),
    path('produtos/', retorna_produtos, name='retorna_produtos'),
    path('produto/<int:pk>/', detalhes_produto, name='detalhes_produto'),
    path('categoria/<int:pk>/', retorna_produtos_categoria, name='categoria'),
    path('addEndereco/', addEndereco, name='addEndereco'),
    path('carrinho/<int:pk>/', retorna_carrinho, name='carrinho'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
