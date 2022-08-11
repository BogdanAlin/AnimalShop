from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect, render

from AnimalShop import forms


def animalDetailView(request):
    if request.method == 'POST':
        form = forms.AnimalDetailForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(animalDetailView)
    else:
        form = forms.AnimalDetailForm()

    return render(request, 'animalDetailsForm.html', {'form': form})


def animalView(request):
    if request.method == 'POST':
        form = forms.AnimalForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(animalView)
    else:
        form = forms.AnimalForm()

    return render(request, 'animalForm.html', {'form': form})
