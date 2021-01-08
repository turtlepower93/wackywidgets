from django.shortcuts import render, redirect
from .models import Widget

def index(request):
    widgets = Widget.objects.all() 
    widgetCount = 0
    for widget in widgets:
        widgetCount += widget.quantity
    return render(request,'index.html', {'widget_list' : widgets, 'widgetCount' : widgetCount})

def add_widget(request):
    print('asdfasdf')
    form = request.POST
    description = form['description']
    quantity = form['quantity']
    Widget.objects.create(description=description, quantity=quantity)
    return redirect('index')

def delete_widget(request, widget_id):
    Widget.objects.get(id=widget_id).delete()
    return redirect('index')