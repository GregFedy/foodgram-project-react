# Generated by Django 3.2.16 on 2022-10-23 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20221017_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='text',
            field=models.TextField(max_length=1000, verbose_name='Описание рецепта'),
        ),
    ]
