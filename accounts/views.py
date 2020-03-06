from django.shortcuts import render


# Create your views here.
def index(request):
    '''return the index.html file'''
    return render(request, 'index.html')
