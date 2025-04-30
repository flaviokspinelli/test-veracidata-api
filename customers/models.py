from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50, verbose_name='nome')
    email = models.EmailField(unique=True, verbose_name='e-mail')
    phone = models.CharField(max_length=20, verbose_name='telefone')
    birthday = models.DateField(verbose_name='data de nascimento')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'