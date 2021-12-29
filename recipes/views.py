from django.shortcuts import render

# Create your views here.
from .forms import RecipeForm

def create_recipe(request):
    if request.method == "GET":
        form = RecipeForm()
        return render(request, 'create_recipe.html', {"form":form})
    elif request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'create_recipe.html', {"form":form})
        
