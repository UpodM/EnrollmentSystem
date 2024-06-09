from django.shortcuts import render

# Create your views here.

def index_user(request):
    return render(request, 'Year_level/index.html')
    