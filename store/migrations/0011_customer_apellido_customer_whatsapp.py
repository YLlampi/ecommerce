# Generated by Django 4.0.4 on 2022-04-29 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_product_price_false'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='apellido',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='whatsapp',
            field=models.CharField(max_length=9, null=True),
        ),
    ]
