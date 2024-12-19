from django.db import models
from datetime import datetime

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return "{} -{}" .format(self.name, self.email)
    
    class Meta:
        verbose_name ='Cliente'
        verbose_name_plural='Clientes'
        ordering = ['-id']


class TypeImmobile(models.TextChoices):
    APARTMENT ='APARTAMENTO','APARTAMENTO'
    KITNET ='KITNET','KITNET'
    HOUSE='CASA','CASA'


class Immobile(models.Model):
    code=models.CharField(max_length=100)
    type_item = models.CharField(max_length=100, choices=TypeImmobile.choices)
    address =models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_locate = models.BooleanField(default =False)

    def __str__(self):
        return "{} -{}" .format(self.code, self.type_item)
    
    class Meta:
        verbose_name ='Imovel'
        verbose_name_plural='Imoveis'
        ordering = ['-id']

class ImmobileImage(models.Model):
    image = models.ImageField('Images', upload_to='images')
    Immobile = models.ForeignKey(Immobile, related_name='imobile_images', on_delete=models.CASCADE)


    def __str__(self):
        return self.Immobile.code 

class RegisterLocation(models.Model):
    immobile = models.ForeignKey(Immobile, on_delete=models.CASCADE, related_name='reg_location')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    dt_start = models.DateTimeField('Início')
    dt_end = models.DateTimeField('Fim')
    create_at = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.client, self.immobile)

    class Meta:
        verbose_name = 'Registrar Locação'
        verbose_name_plural = 'Registrar Locações'
        ordering = ['-id']
