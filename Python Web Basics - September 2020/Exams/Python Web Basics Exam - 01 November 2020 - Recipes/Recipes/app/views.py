from django.shortcuts import render, redirect

from app.form import RecipeForm, RecipeFormReadOnly
from app.models import Recipe


def home_page(request):
    if Recipe.objects.exists():

        recipes = Recipe.objects.all()
        context = {'recipes': recipes}
        return render(request, 'index.html', context)

    else:
        return render(request, 'index.html')


def create_recipe(request):
    if request.method == 'GET':
        form = RecipeForm()
        context = {'form': form}
        return render(request, 'create.html', context)

    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {'form': form}
        return redirect('home page', context)



def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        form = RecipeForm(instance=recipe)
        context = {'recipe': recipe,
                   'form': form}
        return render(request, 'edit.html', context)

    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {'recipe': recipe,
                   'form': form}
        return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        form = RecipeFormReadOnly(instance=recipe)
        context = {'recipe': recipe,
                   'form': form}
        return render(request, 'delete.html', context)

    else:
        recipe.delete()
        return redirect('home page')


def recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredient = recipe.ingredients.split(', ')
    context = {'recipe': recipe,
               'ingredients': ingredient}

    return render(request, 'details.html', context)

