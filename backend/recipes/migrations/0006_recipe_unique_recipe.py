# Generated by Django 3.2.16 on 2022-10-25 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_text'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='recipe',
            constraint=models.UniqueConstraint(fields=('author', 'name', 'text', 'cooking_time'), name='unique_recipe'),
        ),
    ]