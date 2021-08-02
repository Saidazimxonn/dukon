from django.forms import ModelForm
from .models import OrderPharm
class OrderForm(ModelForm):
    class Meta:
        model = OrderPharm
        fields = '__all__'
