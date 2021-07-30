# Generated by Django 2.2 on 2021-07-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0004_auto_20210728_1255'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'user cart', 'verbose_name_plural': 'users cart'},
        ),
        migrations.AlterField(
            model_name='cart',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='add time'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='amount',
            field=models.PositiveIntegerField(default=1, verbose_name='amount'),
        ),
    ]
