from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import project,tag,review
from .form import project_form
# Create your views here.
def display(request):
    dta=project.objects.all()
    return render(request,'base.html',{'data':dta})
def projectdis(request,pk):
    # print("*****")
    # print(type(pk))
    data=project.objects.get(projname=pk)
    tag=data.tags.all()
    print(data)
    return render(request,'projone.html',{'data':data,'data1':tag})
def create_project(request):
    myform=project_form()
    if request.method=='POST':
        data=project_form(request.POST)
        if data.is_valid():
            data.save()
            return redirect('display')
    return render(request,'form.html',{'data':myform})

def update_project(request,pk):
    proj=project.objects.get(projname=pk)
    myform=project_form(instance=proj)
    if request.method=='POST':
        data=project_form(request.POST,instance=proj)
        if data.is_valid():
            data.save()
            return redirect('display')
    return render(request,'form.html',{'data':myform})

def delete_project(request,pk):
    proj=project.objects.get(projname=pk)
    proj.delete()
    return redirect('display')