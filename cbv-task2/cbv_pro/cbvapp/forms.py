from django import forms
from .models import Laptop
class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = "__all__"


    def clean_ram(self):
        ra = self.cleaned_data['ram']
        if ra < 0:
            raise forms.ValidationError('Ram can not be less than 1GB')
        else:
            return ra
        widgets = {

            'company': forms.TextInput({'placeholder': 'lenovo,hp etc '}),
            'model_name': forms.TextInput({'placeholder': 'model_name'}),
            'ram': forms.TextInput({'placeholder': 'RAM in gb'}),
            'rom': forms.TextInput({'placeholder': 'Rom '}),
            'proc': forms.TextInput({'placeholder': 'i3,i5 etc.'}),
            'weight': forms.TextInput({'placeholder': ''})
        }
