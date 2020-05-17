from django.shortcuts import render


def index(request):
    context = {
        'curso':'programação web com django Framework',
        'outro':'outro qualquer coisa',
        'imagem':'https://www.petz.com.br/blog/wp-content/uploads/2017/04/comportamento-dos-gatos-1.jpg',
    }
    """
    Tudo que eu por aqui eu posso acessar lá no index.html. Basta utilizar {{curso}} por exemplo
    """

    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
