from django.shortcuts import render, redirect

from animal.forms import AnimalForm
from animal.models import Animal


def home_page(request):
    if Animal.objects.exists():
        sick_animals = [animal for animal in Animal.objects.all() if not animal.is_cured]
        cured_animals = [animal for animal in Animal.objects.all() if animal.is_cured]


        context = {'sick_animals': sorted(sick_animals, key=lambda x: x.priority[-1]),
                   'cured_animals': cured_animals
                   }

        return render(request, 'home_with_sick_and_cured.html', context)

    else:
        return render(request, 'home_with_no_animals.html')


def cure_animal(request, pk):
    animal = Animal.objects.get(pk=pk)
    animal.is_cured = True
    animal.save()
    return redirect('home page')



def create_animal(request):
    if request.method == 'GET':
        form = AnimalForm()
        context = {'form': form}
        return render(request, 'create.html', context)

    else:
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {'form': form}
        return render(request, 'create.html', context)


def edit_animal(request, pk):
    animal = Animal.objects.get(pk=pk)

    if request.method == 'GET':
        form = AnimalForm(instance=animal)
        context = {'animal': animal,
                   'form': form}
        return render(request, 'edit.html', context)

    else:
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {'animal': animal,
                   'form': form}
        return render(request, 'edit.html', context)


def delete_animal(request, pk):
    animal = Animal.objects.get(pk=pk)

    if request.method == 'GET':
        context = {'animal': animal,
                   }
        return render(request, 'delete.html', context)

    else:
        animal.delete()
        return redirect('home page')


def animal_details(request, pk):
    animal = Animal.objects.get(pk=pk)

    context = {'animal': animal,
               }

    return render(request, 'details.html', context)

