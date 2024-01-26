# Generated by Django 5.0 on 2024-01-26 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=10)),
            ],
        ),
    ]