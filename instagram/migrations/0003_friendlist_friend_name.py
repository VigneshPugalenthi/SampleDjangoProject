# Generated by Django 2.2.4 on 2019-08-23 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_friendlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendlist',
            name='Friend_name',
            field=models.CharField(blank=True, default=None, max_length=30),
        ),
    ]
