# Generated by Django 4.0.2 on 2022-06-23 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaseDatos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idBoleta', models.CharField(max_length=300)),
                ('vendedor', models.CharField(max_length=300)),
                ('fechaVenta', models.DateField()),
                ('montoTotal', models.CharField(max_length=300)),
                ('totalProductos', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Productos2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre2', models.CharField(max_length=300)),
                ('descripcion2', models.CharField(max_length=300)),
                ('disponible2', models.BooleanField()),
                ('fechaIncorporacion2', models.DateField()),
                ('correoProveedor', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idVendedor', models.CharField(max_length=300)),
                ('nombreVendedor', models.CharField(max_length=300)),
                ('fechaCotratacion', models.DateField()),
                ('totalVentas', models.CharField(max_length=300)),
                ('direccion', models.CharField(max_length=300)),
            ],
        ),
    ]
