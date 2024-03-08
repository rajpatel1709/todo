from django.shortcuts import render
from todo.models import Task
def home(request):
    tasks = Task.objects.filter(is_compeleted=False).order_by('-updated_at')
    #it is ascending if -updated_at then descending order
    compeleted_tasks = Task.objects.filter(is_compeleted=True)
    
    context = {
        'tasks':tasks,
        'compeleted_tasks':compeleted_tasks,

    }
    return render(request,'home.html',context)