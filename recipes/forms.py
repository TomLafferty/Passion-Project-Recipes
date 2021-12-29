from django import forms
from .models import Recipe, Ingredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
    
    def clean_servings(self):
        value = self.cleaned_data.get("servings")
        print(value)
        if value < 1:
            raise forms.ValidationError("We are way too hungry for zero servings.")
        return value


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        exclude = ('recipe',)


IngredientFormSet = forms.inlineformset_factory(Recipe, Ingredient, form=IngredientForm)