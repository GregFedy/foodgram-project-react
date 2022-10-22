import decimal

from django.contrib.auth import get_user_model
from django.core.validators import (RegexValidator, MinValueValidator,
                                    MaxValueValidator)
from django.db import models

User = get_user_model()


class Ingredient(models.Model):
    """Модель ингредиента."""
    name = models.CharField(
        'Название ингредиента',
        max_length=200,
        db_index=True
    )
    measurement_unit = models.CharField(
        'Единица измерения',
        max_length=200,
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Tag(models.Model):
    """Модель тега."""
    name = models.CharField(
        'Название тега',
        unique=True,
        max_length=50,
        db_index=True
    )
    color = models.CharField(
        'Цветовой HEX-код',
        unique=True,
        max_length=7,
        validators=[
            RegexValidator(
                regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
                message='Значение не соответствует цвету в формате HEX!'
            )
        ]
    )
    slug = models.SlugField(
        'Cлаг тега',
        unique=True,
        max_length=50,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Модель рецепта."""
    author = models.ForeignKey(
        User,
        related_name='recipes',
        on_delete=models.CASCADE,
        verbose_name='Автор рецепта',
    )
    name = models.CharField('Название рецепта', max_length=200)
    text = models.TextField('Описание рецепта')
    image = models.ImageField(
        'Изображение',
        upload_to='recipes/images'
    )
    cooking_time = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1, message='Минимальное значение 1!'),
            MaxValueValidator(1440, message='Максимальное значение 1440!')
        ],
        verbose_name='Время приготовления, мин.'

    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientRecipe',
        related_name='recipes',
        verbose_name='Ингредиенты'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Теги'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientRecipe(models.Model):
    """Модель количества ингридиентов в рецептах."""
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredient_list',
        verbose_name='Рецепт',
    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
    )
    amount = models.DecimalField(
        'Количество ингредиента',
        default=1,
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(
                decimal.Decimal('0.01'),
                message='Минимальное количество 0.01!'
            ),
            MaxValueValidator(
                decimal.Decimal('1000.00'),
                message='Максимальное значение 1000.00!'
            )
        ]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name='recipe_ingredient_exists',
                fields=['recipe', 'ingredient']
            )]
        verbose_name = 'Ингредиент в рецепте'
        verbose_name_plural = 'Ингредиенты в рецептах'

    def __str__(self):
        return f'{self.recipe}: {self.ingredient} – {self.amount}'


class Favorite(models.Model):
    """Модель избранного."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Рецепт',
    )

    class Meta:
        verbose_name = 'Избранный рецепт'
        verbose_name_plural = 'Избранные рецепты'
        constraints = [
            models.UniqueConstraint(
                name='unique_favorite',
                fields=['user', 'recipe']
            )]

    def __str__(self):
        return f'{self.user} имеет "{self.recipe}" в Избранном'


class ShoppingCart(models.Model):
    """Модель списка покупок."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Рецепт',
    )

    class Meta:
        verbose_name = 'Корзина покупок'
        verbose_name_plural = 'Корзины покупок'
        constraints = [
            models.UniqueConstraint(
                name='unique_shopping_cart',
                fields=['user', 'recipe']
            )]

    def __str__(self):
        return f'{self.user} имеет {self.recipe} в Корзине покупок'
