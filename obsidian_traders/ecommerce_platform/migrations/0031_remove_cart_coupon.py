# Generated by Django 3.0.3 on 2020-08-21 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_platform', '0030_auto_20200821_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='coupon',
        ),
    ]