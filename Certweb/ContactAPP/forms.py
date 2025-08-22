from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        label="Nombre",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@email.com'})
    )
    telefono = forms.CharField(
        max_length=15,
        required=False,
        label="Teléfono",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Opcional'})
    )
    direccion = forms.CharField(
        max_length=200,
        label="Dirección del inmueble",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'})
    )
    mensaje = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Escribe tu mensaje'})
    )
