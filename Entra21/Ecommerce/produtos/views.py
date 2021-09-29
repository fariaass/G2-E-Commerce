from produtos.models import Produto
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Produto
from categorias.models import Tag
from random import randint
from Ecommerce.forms import SearchForm

def retorna_produtos(request):
    """
    Retorna os objetos do modelo Produto.
    """
    if request.method == 'POST':
        return search(request)
    else:
        form = SearchForm()
    dados_lista = Produto.objects.all()

    paginacao = Paginator(dados_lista, 3)
    pagina = request.GET.get('pagina')
    dados = paginacao.get_page(pagina)
    
    return render(request, 'produtos/produtos.html', {'dados':dados, 'form': form})


def retorna_produtos_mais_vendidos(request):
    """
    Esta função retorna um vetor com os 20 produtos mais vendidos, na ordem decrescente,
    utilizando do método de ordenação, bubblesort, o qual compara os itens em pares,
    e realiza trocas entre os mesmos.
    """
    if request.method == 'POST':
        return search(request)
    else:
        form = SearchForm()
    dados_lista = Produto.objects.all()
    dados_lista = produto_queryset_parser(dados_lista)
    bubblesort(dados_lista, len(dados_lista) - 1, 'vendas')

    paginacao = Paginator(dados_lista, 6)
    pagina = request.GET.get('pagina')
    dados = paginacao.get_page(pagina)

    return render(request, 'produtos/produtos.html', {'dados': dados, 'titulo':'Mais Vendidos', 'form': form})


def retorna_produtos_mais_visualizados(request):
    """
    Esta função retorna um vetor com os 20 produtos mais vistos, na ordem decrescente,
    utilizando do método de ordenação, bubblesort, o qual compara os itens em pares,
    e realiza trocas entre os mesmos.
    """
    if request.method == 'POST':
        return search(request)
    else:
        form = SearchForm()
    dados = Produto.objects.all()
    dados = produto_queryset_parser(dados)
    bubblesort(dados, len(dados) - 1, 'visualizacoes')

    paginacao = Paginator(dados, 6)
    pagina = request.GET.get('pagina')
    dados = paginacao.get_page(pagina)

    return render(request, 'produtos/produtos.html', {'dados':dados, 'titulo':'Mais Visitados', 'form':form})


def retorna_produtos_mais_recentes(request):
    """
    Esta função retorna um vetor com os 20 produtos mais recentes cadastrados no banco de dados,
    utilizando os métodos mágicos na classe Produto para fazer a comparação entre as datas,
    essas comparações sendo feitas utilizando a biblioteca datetime.
    """
    if request.method == 'POST':
        return search(request)
    else:
        form = SearchForm()
    dados = Produto.objects.all()
    dados = produto_queryset_parser(dados)
    bubblesort(dados, len(dados) - 1, 'data_criacao')

    paginacao = Paginator(dados, 6)
    pagina = request.GET.get('pagina')
    dados = paginacao.get_page(pagina)

    return render(request, 'produtos/produtos.html', {'dados':dados, 'titulo':'Lançamentos', 'form': form})


def detalhes_produto(request, pk):
    """
    Esta função retorna os dados do produto selecionado.
    """
    if request.method == 'POST':
        return search(request)
    else:
        form = SearchForm()
    produto = get_object_or_404(Produto, pk=pk)
    dados = Produto.objects.all()
    produto.visualizacoes += 1
    produto.save()
    reco = recomendacao(dados, produto)
    if request.user.is_authenticated:
        try:
            if produto in request.user.carrinho.produtos.all():
                in_cart = True
            else:
                in_cart = False
        except:
            in_cart = False
    else:
        try: 
            products = request.session['cart_products']
        except:
            in_cart = False
        else:
            if products.get(str(produto.pk), False):
                in_cart = True
            else:
                in_cart = False

    return render(request, 'produtos/detalhes_produto.html', {'produto': produto, 'dados': reco, 'nome': 'Produto', 'success': False, 'in_cart': in_cart, 'form': form})


def recomendacao(query, exclude):
    """
    Esta função sorteia produtos aleatórios para retornar como recomendação.
    """
    recomendacao_list = []
    for _ in range(3):
        reco = query[randint(0, len(query) - 1)]
        if reco not in recomendacao_list and reco.nome != exclude.nome:
            recomendacao_list.append(reco)
        else:
            while reco in recomendacao_list or reco.nome == exclude.nome:
                reco = query[randint(0, len(query) - 1)]
            recomendacao_list.append(reco)

    return recomendacao_list


def produto_queryset_parser(query, to_session_cart=False):
    """
    Esta função é um parser que pega uma queryset de produto, e retorna um json.
    """
    query_parsed = []
    if to_session_cart:
        for item in query:
            dic = {'id': item['pk'], 'nome': item['fields']['nome'], 'descricao': item['fields']['descricao'], 'preco': item['fields']['preco'], 'imagem': item['fields']['imagem'], 'data_criacao': item['fields']['data_criacao'], 'visualizacoes': item['fields']['visualizacoes'], 'vendas': item['fields']['vendas'], 'is_disponivel': item['fields']['is_disponivel'], 'categoria': item['fields']['categoria'], 'tags': item['fields']['tags']}
            query_parsed.append(dic)
    else:
        for item in query:
            dic = {'id': item.id, 'nome': item.nome, 'descricao': item.descricao, 'preco': item.preco, 'imagem': item.imagem, 'data_criacao': item.data_criacao, 'visualizacoes': item.visualizacoes, 'vendas': item.vendas, 'is_disponivel': item.is_disponivel, 'categoria': item.categoria, 'tags': item.tags}
            query_parsed.append(dic)
    return query_parsed


def produto_instance_parser(item):
    """
    Esta função é um parser que pega uma instancia de um modelo de produto, e retorna um json.
    """
    dic = {'id': item.id, 'nome': item.nome, 'descricao': item.descricao, 'preco': item.preco, 'imagem': item.imagem, 'data_criacao': item.data_criacao, 'visualizacoes': item.visualizacoes, 'vendas': item.vendas, 'is_disponivel': item.is_disponivel, 'categoria': item.categoria, 'tags': item.tags}
    return dic


def bubblesort(v, n, key):
        """
        Esta função é um método de ordenação muito conhecido, onde as informações são comparadas em pares,
        e vão sendo realocadas dependendo do resultado da comparação.
        """
        if n < 1:
            return
        
        for i in range(n):
            if v[i][key] < v[i + 1][key]:
                temp = v[i]
                v[i] = v[i + 1]
                v[i + 1] = temp

        bubblesort(v, n - 1, key)

def search(request):
    """
    Esta função pega os dados do formulário enviado, que é o campo de pesquisa, e então confere se o resultado
    da pesquisa é vazio, se for retorna erro, se não, pesquisa os produtos em que a pesquisa está presente no nome,
    e então quebra a pesquisa, pesquisa as tags com as palavras da pesquisa, entãp confere os itens que se repetiram
    e junta tudo em um vetor só, para retornar ao template que exibe os produtos.
    """
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            result = form.cleaned_data['result']
            products_final = search_at_db(result)
    else:
        result = request.GET.get('search')
        products_final = search_at_db(result)

    form = SearchForm()
    paginacao = Paginator(products_final, 1)
    pagina = request.GET.get('pagina')
    products_final = paginacao.get_page(pagina)
    print(request.GET)
    
    return render(request, 'produtos/produtos.html', {'dados':products_final, 'titulo':'Resultados', 'form': form, 'search': result})

def search_at_db(result):
    products_tags_products_parsed = []
    products_final = []
    result_broke = result.split()
    products = Produto.objects.all().filter(nome__icontains=result)
    products = produto_queryset_parser(products)
    products_tags = Tag.objects.all().filter(nome__in=result_broke)
    products_tags_products = [t.produtos.all() for t in products_tags]
    for qs in products_tags_products:
        qs_parsed = produto_queryset_parser(qs)
        for p in qs_parsed:
            products_tags_products_parsed.append(p)
    products = products + products_tags_products_parsed
    for p in products:
        if p not in products_final:
            products_final.append(p)

    return products_final