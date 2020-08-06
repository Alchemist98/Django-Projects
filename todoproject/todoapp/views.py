from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect 
# Create your views here.
def index(request):
    #We’ll create a new variable to store all the todo items. Then,
    # we’ll return this list to the template file.
    items = TodoListItem.objects.all()
    return render(request,'todolist.html',{'items':items})

def addToView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todoapp/') 

