from django.shortcuts import render, get_list_or_404, get_object_or_404
from produtos.models import Produto
from categorias.models import Categorias
from produtos.forms import SearchForm
from produtos.views import search
from django.core.paginator import Paginator

def retorna_produtos_categoria(request, pk):
    """
    Esta função retorna os produtos de determinada categoria.
    """
    if request.method == 'POST':
        return search(request)
    else:
        form = SearchForm()
        if request.GET.get('search') != '':
            if request.GET.get('pagina') != None:
                return search(request)
    categoria = get_object_or_404(Categorias, pk=pk)
    try:
        produtos = get_list_or_404(Produto, categoria=categoria.id)
    except:
        return render(request, 'erro.html', {'message': 'Não há produtos nesta categoria. Será adicionado em breve.'})
    
    paginacao = Paginator(produtos, 6)
    pagina = request.GET.get('pagina')
    produtos = paginacao.get_page(pagina)

    return render(request, 'produtos/produtos.html', {'dados': produtos, 'titulo':categoria.nome, 'form': form})
