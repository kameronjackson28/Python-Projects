# Generated by Django 2.1.5 on 2021-02-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('entrees', 'entrees'), ('appetizers', 'appetizers'), ('treats', 'treats'), ('drinks', 'drinks')], max_length=60),
        ),
    ]
