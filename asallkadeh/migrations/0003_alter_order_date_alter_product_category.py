# Generated by Django 5.1.1 on 2024-09-04 06:40

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asallkadeh', '0002_order_date_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 9, 4, 11, 10, 1, 199279)),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='asallkadeh.category'),
        ),
    ]
