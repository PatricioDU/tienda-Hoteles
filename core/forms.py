from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Categoria, Producto, Perfil

# *********************************************************************************************************#
#                                                                                                          #
# INSTRUCCIONES PARA EL ALUMNO, PUEDES SEGUIR EL VIDEO TUTORIAL, COMPLETAR EL CODIGO E INCORPORAR EL TUYO: #
#                                                                                                          #
# https://drive.google.com/drive/folders/1ObwMnpKmCXVbq3SMwJKlSRE0PCn0buk8?usp=drive_link                  #
#                                                                                                          #
# *********************************************************************************************************#

# PARA LA PAGINA MANTENEDOR DE PRODUCTOS:
# Crea ProductoForm como una clase que hereda de ModelForm
# asocialo con el modelo Producto
# muestra todos los campos
# crea 2 widgets para:
#   - la descripción del producto como TextArea
#   - el botón de cargar imagen como FileInput y 
#     escóndelo para reemplazarlo por otro acorde 
#     con tu diseño gráfico
# renombra las siguientes etiquetas para que ocupen menos
# espacio en la página: 'Nombre', 'Subscriptor(%)' y 'Oferta(%)'
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(),
            'imagen': forms.FileInput(attrs={'class':'d-none'})
        }
        labels = {
            'nombre': 'Nombre.',
            'descuento_subscriptor': 'Subscriptor(%).',
            'descuento_oferta': 'Oferta(%).'
        }

# El formulario de ingreso está listo, no necesitas modificarlo
class IngresarForm(Form):
    username = forms.CharField(widget=forms.TextInput(), label="Cuenta")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    class Meta:
        fields = ['username', 'password']


# El formulario de bodega está listo, no necesitas modificarlo
class BodegaForm(Form):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), label='Categoría')
    producto = forms.ModelChoiceField(queryset=Producto.objects.none(), label='Producto')
    cantidad = forms.IntegerField(label='Cantidad')
    class Meta:
        fields = '__all__'



# PARA LA PAGINA DE REGISTRO DE NUEVO USUARIO:
class RegistroUsuarioForm(UserCreationForm):
   class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'email': 'E-mail'
        
        }

# PARA LA PAGINA DE REGISTRO DE NUEVO CLIENTE:
class RegistroPerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = ['rut', 'direccion', 'subscrito', 'imagen']
        exclude = ['tipo_usuario']
        widgets = {
            'direccion': forms.Textarea(),
            'imagen': forms.FileInput()
        
        }

# PARA LA PAGINA MIS DATOS Y MANTENEDOR DE USUARIOS:
class UsuarioForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'email': 'E-mail'
        }

class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = ['tipo_usuario', 'rut', 'direccion', 'subscrito', 'imagen']
        widgets = {
            'direccion': forms.Textarea(),
            'imagen': forms.FileInput()
        }