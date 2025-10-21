from django.db import models
 
class motoristas (models.Model):
    nome =  models.CharField(max_length=50)
    idade= models.IntegerField()
    foto= models.ImageField(upload_to=('fotos'))
    ativo= models.BooleanField(default='True')

    def __str__(self):
        return self.nome