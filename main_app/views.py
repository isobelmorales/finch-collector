from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# Import Finch model
from .models import Finch, Toy
from .forms import FeedingForm

# Define the home view
def home(request):
    return render(request, 'home.html')

# Define the about view
def about(request):
    return render(request, 'about.html')

# Define the finches index view
def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

# Finches detail route
def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)

     # first we'll get a list of ids of toys the finch owns
    id_list = finch.toys.all().values_list('id')
    # then we'll make a list of the toys the finch does not have
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)

    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()

    return render(request, 'finches/detail.html', { 'finch': finch, 'feeding_form': feeding_form, 'toys': toys_finch_doesnt_have })

# Create finch view
class FinchCreate(CreateView):
    model = Finch
    fields='__all__'

# Update Finch
class FinchUpdate(UpdateView):
    model = Finch
    # let's use custom fields to disallow renaming a finch
    fields = ['habitat', 'food', 'nesting', 'behavior', 'conservation']

# Delete Finch
class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

# Add Feeding
def add_feeding(request, finch_id):
    # create a ModelForm instance from the data in request.POST
    form = FeedingForm(request.POST)

    # we need to validate the form, that means "does it match our data?"
    if form.is_valid():
        # we dont want to save the form to the db until is has the finch id
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

def assoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.remove(toy_id)
    return redirect('detail', finch_id=finch_id)

# ToyList
class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'

# ToyDetail
class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'

# ToyCreate
class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']

    # define what the inherited method is_valid does(we'll update this later)
    def form_valid(self, form):
        # we'll use this later, but implement right now
        # we'll need this when we add auth
        # super allows for the original inherited CreateView function to work as it was intended
        return super().form_valid(form)

# ToyUpdate
class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

# ToyDelete
class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'