from django import forms
from .models import Producto, Cliente

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
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'correo']  # 👈 si no quieres mostrar "activo"

        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Nombre completo",
                "class": "form-control"
            }),
            "correo": forms.EmailInput(attrs={
                "placeholder": "Correo electrónico",
                "class": "form-control"
            }),
        }
