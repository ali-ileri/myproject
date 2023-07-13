from django import forms
from .models import Kaynak

class KaynakForm(forms.ModelForm):
    class Meta:
        model = Kaynak
        fields = '__all__'  # Tüm alanları kullanmak için '__all__' kullanılır
