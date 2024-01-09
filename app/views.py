from django.shortcuts import render

# Create your views here.
from .forms import *
from .models import *
from django.http import HttpResponse



def create_school(request):
    ESFO = SchoolForm()
    d = {'ESFO':ESFO}
    
    if request.method=='POST':
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid():
            n = SFDO.cleaned_data['Sname']
            sp = SFDO.cleaned_data['S_Principal']
            sl = SFDO.cleaned_data['S_Loc']
            e = SFDO.cleaned_data['Email']
            re = SFDO.cleaned_data['ReEnter_Email']
            
            SO = School.objects.get_or_create(Sname=n,Sprincipal=sp,Sloc=sl,email=e,reEnterEmail=re)[0]
            SO.save()
            
            return HttpResponse(f'{n} created successfully!!!')
        else:
            return HttpResponse('Invalid Input')
    
    
    return render(request,'create_school.html',d)