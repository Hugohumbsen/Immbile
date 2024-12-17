from django import forms
from .models import Client, Immobile

## Cadastra Cliente
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def __init__(self, *args, **kwargs):  # Adiciona
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ImmobileForm(forms.ModelForm):
    Immobile = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
    class Meta:
        model = Immobile
        fields = '__all__'
        exclude = ['is_locate']

    def __init__(self, *args, **kwargs):
        super(ImmobileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.__class__.__name__ in ('CheckboxInput', 'RadioSelect'):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'  # FORMMYAAP