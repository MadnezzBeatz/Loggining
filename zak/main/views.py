from django.shortcuts import render
def index(request):
    data = {
        'tittle': 'Главная страница',

    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')
# Create your views here.
