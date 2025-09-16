from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio']

        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Nombre del producto"
            }),
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Breve de descripción"
            }),
            "precio": forms.NumberInput(attrs={
                "step": "0.01",
                "min": 0
            })
        }
