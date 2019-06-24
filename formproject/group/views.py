from django.shortcuts import render

def index(request):
    return render(request, 'group/index.html')

def Create(request):
    return render(request, 'group/create.html')

def delete(request, pk):
    return render(request, 'home')

def edit(request, pk):
    return render(request, 'group/edit.html')

def detail(request, pk):
    return render(request, 'group/detail.html')





# Create your views here.
