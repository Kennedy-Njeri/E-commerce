# Generated by Django 2.2.1 on 2019-09-05 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0018_coupon_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='amount',
        ),
    ]
