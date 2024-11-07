# Generated by Django 5.1.3 on 2024-11-07 23:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='ong',
            name='endereco',
            field=models.CharField(blank=True, default='Rua', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ong',
            name='usuario',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ong', to=settings.AUTH_USER_MODEL),
        ),
    ]
