from django.shortcuts import render
from django.utils.timezone import make_aware
from django.utils.dateparse import parse_datetime
from todo.models import Task

# Create your views here.
def index(request):
    if request.method == "POST":
        title = request.POST.get('title')
        due_at = request.POST.get('due_at')
        if title:
            Task.objects.create(title=title, due_at=due_at or None)
            # return redirect('/')  # テストのためコメントアウト

    if request.GET.get('order') == 'due':
        tasks = Task.objects.order_by('due_at')
    else:
        tasks = Task.objects.order_by('-posted_at')

    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)