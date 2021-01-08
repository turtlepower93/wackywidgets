from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def add_widget(request):
    pass