# Generated by Django 4.2.14 on 2024-11-06 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_formulario'),
    ]

    operations = [
        migrations.AddField(
            model_name='formulario',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2024, 11, 6, 15, 51, 57, 741692, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
