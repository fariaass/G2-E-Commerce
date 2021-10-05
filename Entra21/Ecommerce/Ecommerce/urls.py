from django.urls.conf import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls.static import static
from . import settings
from .views import home
import produtos.urls
import categorias.urls
import accounts.urls
import carrinho.urls
import pedidos.urls

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('allauth.socialaccount.providers.google.urls')),
    path('accounts/', include('allauth.socialaccount.providers.twitter.urls')),
    path('accounts/', include('allauth.urls'), name='socialaccount_signup'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/', include(accounts.urls, namespace='users')),
    path('produtos/', include(produtos.urls)),
    path('categorias/', include(categorias.urls)),
    path('carrinho/', include(carrinho.urls)),
    path('pedidos/', include(pedidos.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)