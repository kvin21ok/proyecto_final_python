from django import forms
from ejemplo.models import (Familiar, Mascota, Empleo)

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=20,
                            widget=forms.TextInput(attrs={'placeholder':'Busque algo...'}))

class FamiliarForm(forms.ModelForm):
    class Meta:
        model = Familiar
        fields = ['nombre', 'direccion', 'numero_pasaporte']

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'tipo', 'edad']

class EmpleoForm (forms.ModelForm):
    class Meta:
        model = Empleo
        fields = ['ocupacion', 'antiguedad', 'cargo', 'breve_descripcion']