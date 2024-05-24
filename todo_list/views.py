from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDoList, Item

def index(request):
    todo_lists = ToDoList.objects.all()
    return render(request, 'todo_list/index.html', {'todo_lists': todo_lists})

def create_list(request):
    if request.method == 'POST':
        name = request.POST['name']
        todo_list = ToDoList.objects.create(name=name)
        return redirect('index')
    return render(request, 'todo_list/create_list.html')

def add_item(request, list_id):
    todo_list = get_object_or_404(ToDoList, id=list_id)
    if request.method == 'POST':
        description = request.POST['description']
        Item.objects.create(todo_list=todo_list, description=description)
        return redirect('index')
    items = Item.objects.filter(todo_list=todo_list)
    return render(request, 'todo_list/add_item.html', {'todo_list': todo_list, 'items': items})

def list_items(request):
    todo_lists = ToDoList.objects.all()
    items_by_list = {}
    for todo_list in todo_lists:
        items_by_list[todo_list] = Item.objects.filter(todo_list=todo_list)
    return render(request, 'todo_list/list_items.html', {'items_by_list': items_by_list})