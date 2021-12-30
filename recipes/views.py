from django.shortcuts import render, redirect

# Create your views here.
from .forms import RecipeForm, IngredientFormSet
from django.shortcuts import render

from .forms import CommentForm
from .models import Recipe, Ingredient

def create_recipe(request):
    if request.method == "GET":
        form = RecipeForm()
        formset = IngredientFormSet()
        return render(request, 'create_recipe.html', {"form":form, "formset":formset})


    elif request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            formset = IngredientFormSet(request.POST, instance=recipe)
            if formset.is_valid():
                formset.save()
            return redirect('/')
        else:
            return render(request, 'create_recipe.html', {"form":form})
        



def recipes_index(request):
    posts = Recipe.objects.all().order_by("-created_on")
    context = {"posts": posts}
    return render(request, "recipes_index.html", context)


def recipes_category(request, category):
    posts = Recipe.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    context = {"category": category, "posts": posts}
    return render(request, "recipes_category.html", context)


def recipes_detail(request, pk):
    post = Recipe.objects.get(pk=pk)
    comments = Ingredient.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Ingredient(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()

    context = {"post": post, "comments": comments, "form": form}
    return render(request, "recipes_detail.html", context)