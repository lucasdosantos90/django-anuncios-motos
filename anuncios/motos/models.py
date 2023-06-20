from django.db import models
from PIL import Image

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

class Marca(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Opcional(models.Model):
    opcional = models.CharField(max_length=30)

    def __str__(self):
        return self.opcional

class Combustivel(models.Model):
    combustivel = models.CharField(max_length=30)

    def __str__(self):
        return self.combustivel


class Moto(models.Model):
    nome = models.CharField(max_length=30)
    preco = models.CharField(max_length=7)
    modelo = models.CharField(max_length=30,default='Honda')
    ano = models.CharField(max_length=4, default='2014')
    cor = models.CharField(max_length=30, default='Prata')
    km = models.CharField(max_length=30, default='0')
    combustivel = models.ManyToManyField(Combustivel)
    informacoes = models.TextField()
    tags = models.ManyToManyField(Tag)
    foto_principal = models.ImageField(default='default.jpg',upload_to='media',null=False, blank=False)
    foto_1 = models.ImageField(default='default.jpg',upload_to='media',null=True, blank=True)
    foto_2 = models.ImageField(default='default.jpg',upload_to='media',null=True, blank=True)
    foto_3 = models.ImageField(default='default.jpg',upload_to='media',null=True, blank=True)
    foto_4 = models.ImageField(default='default.jpg',upload_to='media',null=True, blank=True)

    marca = models.ManyToManyField(Marca)
    opcionais = models.ManyToManyField(Opcional)

    def save(self, *args, **kwargs):
        super(Moto,self).save(*args, **kwargs)

        img = Image.open(self.foto_principal.path)
        if img.height > 1920 and img.width > 980:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.foto_principal.path)
        img1 = Image.open(self.foto_1.path)
        if img1.height > 1920 and img1.width > 980:
            output_size = (300,300)
            img1.thumbnail(output_size)
            img1.save(self.foto_1.path) 
        img2 = Image.open(self.foto_2.path)
        if img2.height > 1920 and img2.width > 980:
            output_size = (300,300)
            img2.thumbnail(output_size)
            img2.save(self.foto_2.path)
        img3 = Image.open(self.foto_3.path)
        if img3.height > 1920 and img3.width > 980:
            output_size = (300,300)
            img3.thumbnail(output_size)
            img3.save(self.foto_3.path) 
        img4 = Image.open(self.foto_4.path)
        if img4.height > 1920 and img4.width > 980:
            output_size = (300,300)
            img4.thumbnail(output_size)
            img4.save(self.foto_4.path)                        

              


    def __str__(self):
        return self.nome


