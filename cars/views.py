from django.shortcuts import render, redirect
from django.views import View
from cars.models import Car
from cars.forms import CarModelForm
# Create your views here.

class CarsView(View):
    def get(self, request):
        cars = Car.objects.all().order_by("-factory_year")
        search = request.GET.get('search')
    
        if search:
            cars = cars.filter(model__icontains = search)

        return render(
            template_name='cars.html', 
            request=request, 
            context={'cars': cars}
        )
    

class NewCarView(View):

    def get(self, request):
        new_car_form = CarModelForm()
        return render(request, 'new_car.html', {'new_car_form': new_car_form})
        
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('car_list')
        return render(request, 'new_car.html', {'new_car_form': new_car_form})