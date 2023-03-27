from django.shortcuts import render, redirect 
from .models import *
from .forms import *
# Create your views here.
def home(request):
    post = Company.objects.all()
    context = {
        'post':post
    }
    return render(request, 'index.html',context)

def add(request):
    form = CompanyForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CompanyForm()
    
    context = {
        'form':form
    }
    return render(request, 'addcompany.html', context)

def delete(request, id):
    post = Company.objects.get(id=id)
    post.delete()
    return redirect('home')

def edit(request, id):
    post = Company.objects.get(id=id)
    context = {
        'post':post
    }

    return render(request, 'update.html', context)

def editrecord(request, id):
    name = request.POST['name']
    about = request.POST['about']
    logo  = request.POST['logo']

    malumot = Company.objects.get(id=id)
    malumot.name = name
    malumot.about = about
    malumot.logo = logo 
    malumot.save()
    return redirect('home')