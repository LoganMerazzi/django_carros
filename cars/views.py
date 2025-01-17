from django.shortcuts import render
from cars.models import Car
# Create your views here.



def cars_view(request):
    cars = Car.objects.all()
    print(cars)
    #contexto = Car.objects.filter(brand__name='fiat')
    #print(contexto)
    
    return render(
        template_name='cars.html', 
        request=request, 
        context={'cars': cars}
        #context={'cars': contexto}
        
    )