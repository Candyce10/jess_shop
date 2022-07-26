
# Generated by Django 4.0.4 on 2022-07-22 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=1000)),
                ('ingredients', models.TextField(max_length=1000)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]