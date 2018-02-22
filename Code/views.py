from django.shortcuts import render

# Create your views here.
def index(request):
    empty = ' '
    context = {empty: '  '}
    return render(request, 'Code/index.html', context)