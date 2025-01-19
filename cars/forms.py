from django import forms
from cars.models import Brand, Car
    
class CarModelForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = '__all__'

    # para validações de campos, as funções obrigatoriamente devem iniciar com "clean_"
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 20000:
            self.add_error('price', 'Valor mínimo do carro deve ser de R$20.000,00')
        return price
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Ano de fabricação inválido')
        return factory_year