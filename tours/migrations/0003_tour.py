# Generated by Django 3.2.3 on 2021-05-26 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=145)),
                ('slug', models.CharField(blank=True, max_length=45, null=True)),
                ('operador', models.CharField(blank=True, max_length=45, null=True)),
                ('tipoDeTour', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=256, null=True)),
                ('img', models.CharField(blank=True, max_length=256, null=True)),
                ('pais', models.CharField(blank=True, max_length=45, null=True)),
                ('zonaLlegada', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tours_llegada', to='tours.zona')),
                ('zonaSalida', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tours_salida', to='tours.zona')),
            ],
        ),
    ]
