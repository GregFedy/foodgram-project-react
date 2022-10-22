from django.contrib import admin
from django.contrib.admin import display

from .models import (Favorite, Ingredient, IngredientRecipe, Recipe,
                     ShoppingCart, Tag)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Кастомизация админ панели (управление рецептами)."""
    list_display = ('name', 'author', 'added_in_favorites')
    readonly_fields = ('added_in_favorites',)
    list_filter = ('author', 'name', 'tags',)

    @display(description='Количество в избранных')
    def added_in_favorites(self, obj):
        return obj.favorites.count()


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Кастомизация админ панели (управление ингредиентами)."""
    list_display = ('name', 'measurement_unit',)
    list_filter = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Кастомизация админ панели (управление тегам)."""
    list_display = ('name', 'color', 'slug',)


@admin.register(IngredientRecipe)
class IngredientRecipeAdmin(admin.ModelAdmin):
    """Кастомизация админ панели (управление ингридиентами в рецептах)."""
    list_display = ('recipe', 'ingredient', 'amount',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Кастомизация админ панели (управление избранныи рецептами)."""
    list_display = ('user', 'recipe',)


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """Кастомизация админ панели (управление покупками)."""
    list_display = ('user', 'recipe',)
