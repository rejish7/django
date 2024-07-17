# Generated by Django 5.0.6 on 2024-07-17 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=50)),
                ('Address', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
                ('Country', models.CharField(max_length=100)),
            ],
        ),
    ]
