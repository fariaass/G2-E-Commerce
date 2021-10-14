from django.shortcuts import render
from categorias.models import Categorias
from produtos.forms import SearchForm
from produtos.views import search
from random import shuffle

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

    categorias = Categorias.objects.all()
    categorias = categorias_queryset_parser(categorias)
    shuffle(categorias)

    return render(request, 'home.html', {'categorias': categorias, 'form': form})


def categorias_queryset_parser(query):
    """
    Esta função é um parser que pega uma queryset de categoria, e retorna um json.
    """
    query_parsed = []
    for item in query:
        dic = {'id': item.id, 'nome': item.nome, 'imagem': item.imagem}
        query_parsed.append(dic)
    return query_parsed
