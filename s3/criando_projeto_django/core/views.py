from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Produto


def index(request):

    produtos = Produto.objects.all()
    context = {
        'curso':'programação web com django Framework',
        'outro':'outro qualquer coisa',
        'imagem':'https://www.petz.com.br/blog/wp-content/uploads/2017/04/comportamento-dos-gatos-1.jpg',
        'produtos': produtos
    }

    """
    Tudo que eu por aqui eu posso acessar lá no index.html. Basta utilizar {{curso}} por exemplo
    """

    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    # print(f'PK: {pk}')

    #prod = Produto.objects.get(id=pk)
    # print(prod.nome)

    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto':prod
    }
    return render(request, 'produto.html', context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)

