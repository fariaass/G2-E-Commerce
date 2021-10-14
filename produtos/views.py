from produtos.models import Produto
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Produto
from categorias.models import Categorias, Tag
from random import randint
from produtos.forms import SearchForm

def retorna_produtos(request):
    """
    Retorna os objetos do modelo Produto.
    """
    if request.method == 'POST':
        return search(request)
    else:
        form = SearchForm()
        
    dados = Produto.objects.all()

    paginacao = Paginator(dados, 6)
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
        if request.GET.get('pagina') != None:
            return search(request)
        dados = Produto.objects.all()
        dados = produto_queryset_parser(dados)
        bubblesort(dados, len(dados) - 1, 'vendas')

    paginacao = Paginator(dados, 6)
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
        if request.GET.get('pagina') != None:
            return search(request)
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
        if request.GET.get('pagina') != None:
                return search(request)
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
        if request.GET.get('pagina') != None:
            return search(request)
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
    if len(query) < 3:
        return query
    else:
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
    da pesquisa é vazio, se for retorna erro, se não, chama uma função para a pesquisa no banco de dados, e então retorna um template
    com paginação feita.
    """
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            result = form.cleaned_data['result']
            products_final = search_in_db(result)
            if products_final:
                pagina = 1
            else:
                return render(request, 'erro.html', {'message':'Nenhum resultado encontrado para sua pesquisa.'})
    else:
        result = request.GET.get('search')
        products_final = search_in_db(result)
        pagina = request.GET.get('pagina')

    form = SearchForm()
    paginacao = Paginator(products_final, 6)
    products_final = paginacao.get_page(pagina)
    
    return render(request, 'produtos/produtos.html', {'dados':products_final, 'titulo':'Resultados', 'form': form, 'search': result})

def search_in_db(result):
    """
    Esta função utilitária faz a pesquisa no banco de dados através do nome do produto, das tags e das categorias (ainda por fazer).
    Retorna uma lista com os resultados.
    """

    # Inicializa as listas

    products_tags_products_parsed = []
    products_categories_products_parsed = []
    products_final = []

    # Quebra a pesquisa em uma lista de palavras

    result_broke = result.split()
    
    # Confere se o nome do produto contem a pesquisa
    
    products = Produto.objects.all().filter(nome__icontains=result)
    products = produto_queryset_parser(products)
    
    # Confere em todas as tags, se elas estiverem presentes na pesquisa e na pesquisa quebrada
    
    products_tags_1 = Tag.objects.all().filter(nome__icontains=result)
    products_tags_2 = Tag.objects.all().filter(nome__in=result_broke)

    # Pega os produtos das tags, formata eles em json, e adiciona em uma lista
    
    products_tags_products_1 = [t.produtos.all() for t in products_tags_1]
    products_tags_products_2 = [t.produtos.all() for t in products_tags_2]
    products_tags_products = products_tags_products_1 + products_tags_products_2

    for qs in products_tags_products:
        qs_parsed = produto_queryset_parser(qs)
        for p in qs_parsed:
            products_tags_products_parsed.append(p)
            
    # Pega os produtos das categorias, se elas estiverem presentes na pesquisa e na pesquisa quebrada
    
    products_categories_1 = Categorias.objects.all().filter(nome__icontains=result)
    products_categories_2 = Categorias.objects.all().filter(nome__in=result_broke)
    
    # Pega os produtos das categorias, formata eles em json, e adiciona em uma lista
    
    products_categories_products_1 = [t.produtos.all() for t in products_categories_1]
    products_categories_products_2 = [t.produtos.all() for t in products_categories_2]
    products_categories_products = products_categories_products_1 + products_categories_products_2

    for qs in products_categories_products:
        qs_parsed = produto_queryset_parser(qs)
        for p in qs_parsed:
            products_categories_products_parsed.append(p)
            
    # Junta os produtos achados na pesquisa, com os produtos achados nas tags e nas categorias
    
    products = products + products_tags_products_parsed + products_categories_products_parsed
    
    # Anula as repetições e adiciona na lista final, que será retornada
    
    for p in products:
        if p not in products_final:
            products_final.append(p)

    return products_final