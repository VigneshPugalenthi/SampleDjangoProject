# Generated by Django 2.2.4 on 2019-08-22 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('Number', models.PositiveIntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Image', models.ImageField(blank=True, default='default.jpg', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tweet', models.TextField(blank=True, default=None, null=True)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Profile', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('Posts_image', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('Posts_video', models.FileField(blank=True, default=None, null=True, upload_to='')),
                ('User', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='instagram.SignUp')),
            ],
        ),
    ]