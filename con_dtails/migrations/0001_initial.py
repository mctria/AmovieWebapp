# Generated by Django 3.2.9 on 2022-06-17 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='con_dtls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('site', models.CharField(blank=True, max_length=200)),
                ('msg', models.CharField(max_length=5000)),
            ],
        ),
    ]
