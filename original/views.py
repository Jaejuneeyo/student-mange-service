from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from . models import student_models
from original.models import StudentModel
# Create your views here.

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    regi_form = UserCreationForm()     
    if request.method =="POST":
        filled_form = UserCreationForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('home')

    return render(request,'signup.html',{'regi_form' : regi_form})

def create(request):
    if request.method =="POST" :
        item = StudentModel()
        
        item.name = request.POST['name']
        item.major = request.POST['major']
        item.admission_year = request.POST['admission_year']
        item.class_number = request.POST['class_number']
        item.grade = request.POST['grade']
        item.user =request.user
        
        item.save()

        return redirect('home')
    
    return render(request,"create.html")

def update(request, student_id):
    item = get_object_or_404(StudentModel, pk=student_id)
    if request.method =='POST':
        item.name = request.POST['name']
        item.major = request.POST['major']
        item.admission_year = request.POST['admission_year']
        item.class_number = request.POST['class_number']
        item.grade = request.POST['grade']
        item.save()

def detail(request, student_id):
    item = get_object_or_404(StudentModel, pk=student_id)

    return render(request,'detail.html', {'item':item})

def delete(request, student_id):
    item=get_object_or_404(StudentModel, pk=student_id)
    item.delete()

    return redirect('home')