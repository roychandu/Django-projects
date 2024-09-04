from django.shortcuts import render

# Create your views here.
from .models import Task

def task_list(request):
    status_filter = request.GET.get('status')
    sort_by = request.GET.get('sort_by')

    tasks = Task.objects.all()

    if status_filter:
        tasks = tasks.filter(status=status_filter)

    if sort_by == 'priority':
        tasks = tasks.order_by('priority')
    elif sort_by == 'due_date':
        tasks = tasks.order_by('due_date')

    context = {
        'tasks': tasks,
        'status_filter': status_filter,
        'sort_by': sort_by,
    }

    return render(request, 'app/index.html', context)
