# Generated by Django 4.2.4 on 2023-09-12 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_payment_intent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_intent',
        ),
    ]
