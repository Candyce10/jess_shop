# Generated by Django 4.0.4 on 2022-08-10 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_billingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ship',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
