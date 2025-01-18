from django.shortcuts import render
from cars.models import Car
# Create your views here.



def cars_view(request):
    
    print(request)
    print(request.GET)
    print(request.GET.get('search'))

    # Para retorar tudo (select * from...)
    cars = Car.objects.all().order_by('model_year') # para ordernar de forma descrescente, colocar o sinal '-' no nome da coluna a ser ordenada.
    #print(cars)
    
    # Para realizar um filtro.
    # Filtrando diretamente a tabela - case sensitive
    #contexto = Car.objects.filter(model='Gol')

    modelo = request.GET.get('search')
    
    # if para validar se algo foi preenchido com o parametro search na url
    if modelo:
        # Filtrando usando coringas (model like '%%') - case insensitive - apenas considera acentuação
        cars = Car.objects.filter(model__contains=modelo).order_by('model')
    
    # Filtrando dados através de uma FK:
    #contexto = Car.objects.filter(brand__name='Fiat')
    print(cars)
    
    
    
    return render(
        template_name='cars.html', 
        request=request, 
        context={'cars': cars}
        
    )