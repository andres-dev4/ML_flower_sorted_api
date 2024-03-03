# Generated by Django 5.0.2 on 2024-03-03 00:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlmodel', '0002_rename_datosarray_history_predictions'),
    ]

    operations = [
        migrations.AddField(
            model_name='history_predictions',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='history_predictions',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
