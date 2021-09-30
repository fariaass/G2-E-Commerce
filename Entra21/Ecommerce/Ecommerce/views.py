from django.shortcuts import render
from categorias.models import Categoria
from Ecommerce.forms import SearchForm
from produtos.views import search
from django.core.paginator import Paginator

def home(request):
    """
    Esta função retorna as categorias, para a página inicial.
    """
    if request.method == 'POST':
        return search(request)
    else:
        form = SearchForm()
        pagina = request.GET.get('pagina')
        if pagina != None:
            return search(request)

    categorias = Categoria.objects.all()

    return render(request, 'home.html', {'categorias': categorias, 'form': form})
