from django.shortcuts import render

# finches dictionary ("seed")
finches = [
    {'name': 'American Goldfinch', 'habitat': 'Open Woodlands', 'food': 'Seeds', 'nesting': 'Shrub', 'behavior': 'Foliage Gleaner', 'conservation': 'Low Concern'},
    {'name': 'Black Rosy-Finch', 'habitat': 'Tundra', 'food': 'Seeds', 'nesting': 'Ground', 'behavior': 'Ground Forager', 'conservation': 'Red Watch List'}
]

# Define the home view
def home(request):
    return render(request, 'home.html')

# Define the about view
def about(request):
    return render(request, 'about.html')

# Define the finches index view
def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })