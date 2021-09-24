from django.shortcuts import render, get_list_or_404, get_object_or_404
from produtos.models import Produto
from categorias.models import Categoria

def retorna_produtos_categoria(request, pk):
    """
    Esta função retorna os produtos de determinada categoria.
    """
    categoria = get_object_or_404(Categoria, pk=pk)
    produtos = get_list_or_404(Produto, categoria=categoria.id)
    return render(request, 'produtos/produtos.html', {'dados': produtos, 'titulo':categoria.nome})

def categoria_queryset_parser(query):
    """
    Esta função é um parser que pega uma queryset de categoria, e retorna um json.
    """
    query_parsed = []
    for item in query:
        dic = {'id': item.id, 'nome': item.nome, 'imagem': item.imagem}
        query_parsed.append(dic)
    return query_parsed