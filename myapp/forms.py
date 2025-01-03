from django import forms
from .models import Client, Immobile, RegisterLocation

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
                field.widget.attrs['class'] = 'form-control'  



class RegisterLocationForm(forms.ModelForm):
    dt_start = forms.DateTimeField(widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}))
    dt_end = forms.DateTimeField(widget=forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}))

    class Meta:
        model = RegisterLocation
        fields = '__all__'
        exclude = ('immobile', 'create_at',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
