# Generated by Django 3.2.19 on 2023-06-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Combustivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combustivel', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='moto',
            name='ano',
            field=models.CharField(default='2014', max_length=4),
        ),
        migrations.AddField(
            model_name='moto',
            name='cor',
            field=models.CharField(default='Prata', max_length=30),
        ),
        migrations.AddField(
            model_name='moto',
            name='km',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='moto',
            name='modelo',
            field=models.CharField(default='Honda', max_length=30),
        ),
        migrations.AddField(
            model_name='moto',
            name='combustivel',
            field=models.ManyToManyField(to='motos.Combustivel'),
        ),
    ]
