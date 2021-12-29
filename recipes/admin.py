from django.contrib import admin

# Register your models here.

from .models import Recipe, Ingredient

admin.site.register(Recipe)


class IngredientInline(admin.TabularInline):
    model = Ingredient

# @admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, ]