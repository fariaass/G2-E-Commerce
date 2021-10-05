from django.shortcuts import render
from categorias.models import Categoria
from Ecommerce.forms import SearchForm
from produtos.views import search

def home(request):
    """
    Esta função retorna as categorias, para a página inicial, caso não seja solicitada um busca, caso contrário,
    a função de busca é chamada. Em caso da request ser um GET, é feita a conferência para saber se a solicitação
    se passa de uma solicitação de paginação, ou para voltar para a home.
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
