from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.urls import reverse
from .models import TaskTable
from .forms import TaskTableForm

def index_page(request):
    tasktable_fetch_data = TaskTable.objects.filter(completed = False)
    completed_task_data = TaskTable.objects.filter(completed = True)
    context = {
        'tasktable_fetch_data' : tasktable_fetch_data,
        'completed_task_data' : completed_task_data,
    }    
    return render(request, 'myapp/index.html', context)
    
def get_and_save_form_data(request):
    if request.method == 'POST':
        task_from_form = request.POST.get('addtask')
        if task_from_form.strip():  # Check if task_from_form is not empty
            obj_of_tasktable = TaskTable(task_column=task_from_form)
            obj_of_tasktable.save()
        return HttpResponseRedirect(reverse('index_page'))
    #return index_page(request) 
    return redirect('index_page')    
    
def get_and_search_form_data(request):
    search_term = request.GET.get('searchtask')
    if search_term.strip():
        tasktable_search_data = TaskTable.objects.filter(task_column__icontains=search_term)
        context = {'tasktable_search_data': tasktable_search_data}
        return render(request, 'myapp/index.html', context)
    #return index_page(request)
    return redirect('index_page')


def task_delete(request, task_id):
    task = get_object_or_404(TaskTable, id=task_id)
    task.delete()
    return redirect('index_page')

def task_complete(request, task_id):
    task = get_object_or_404(TaskTable, id=task_id)
    task.completed = True
    task.save()
    return redirect('index_page')
    
def task_uncomplete(request, task_id):
    task = get_object_or_404(TaskTable, id=task_id)
    task.completed = False
    task.save()
    return redirect('index_page')

# have to modify following code
def task_edit(request, task_id):
    valueoftask_id = get_object_or_404(TaskTable, id=task_id)
    TaskTableFormObj = TaskTableForm(request.POST, instance=valueoftask_id)
    if TaskTableFormObj.is_valid():
        TaskTableFormObj.save()
        return HttpResponseRedirect(reverse('index_page'))
    else:
        valueoftask_id = get_object_or_404(TaskTable, id=task_id)
        TaskTableFormObj = TaskTableForm(instance = valueoftask_id)    
    context = {
        "form" : TaskTableFormObj
    }    
         
    return render(request, "myapp/edit_task.html", context)