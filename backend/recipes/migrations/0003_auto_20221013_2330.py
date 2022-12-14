# Generated by Django 3.2.16 on 2022-10-13 20:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientRecipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Минимальное количество 1!'), django.core.validators.MaxValueValidator(1000, message='Максимальное значение 1000!')], verbose_name='Количество ингредиента')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient', verbose_name='Ингредиент')),
            ],
            options={
                'verbose_name': 'Ингредиент в рецепте',
                'verbose_name_plural': 'Ингредиенты в рецептах',
            },
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Название тега'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Cлаг тега'),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название рецепта')),
                ('text', models.TextField(verbose_name='Описание рецепта')),
                ('image', models.ImageField(upload_to='recipes/images', verbose_name='Изображение')),
                ('cooking_time', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Минимальное значение 1!'), django.core.validators.MaxValueValidator(1440, message='Максимальное значение 1440!')], verbose_name='Время приготовления, мин.')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор рецепта')),
                ('ingredients', models.ManyToManyField(related_name='recipes', through='recipes.IngredientRecipe', to='recipes.Ingredient', verbose_name='Ингредиенты')),
                ('tags', models.ManyToManyField(related_name='recipes', to='recipes.Tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='ingredientrecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_list', to='recipes.recipe', verbose_name='Рецепт'),
        ),
        migrations.AddConstraint(
            model_name='ingredientrecipe',
            constraint=models.UniqueConstraint(fields=('recipe', 'ingredient'), name='recipe_ingredient_exists'),
        ),
    ]
