# Generated by Django 3.2.4 on 2021-09-16 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='')),
                ('productname', models.CharField(max_length=100)),
            ],
        ),
    ]
