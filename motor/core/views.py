from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contato(request):
    context = {
    'nome': 'MotorWeb',
    'fone': '17189237198731',
    'email': 'motorweb@teste.com.br'
}

    return render(request, 'contato.html', context)