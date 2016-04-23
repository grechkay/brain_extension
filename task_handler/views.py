from django.shortcuts import render, get_object_or_404
from django.contrib import messages, auth
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from datetime import datetime,timedelta

def base_view(request):
    if request.method == "POST":
        task_type = request.POST.get('task_type')
        
        if task_type == 'deadline':
            task_id = request.POST.get('task_id')
            task_to_finish = DeadlineTask.objects.get(id=task_id)
            task_to_finish.active = False
            task_to_finish.save()
        elif task_type == 'deadline_cancel':
            task_id = request.POST.get('task_id')
            task_to_finish = DeadlineTask.objects.get(id=task_id)
            task_to_finish.active = False
            task_to_finish.save()
        elif task_type == 'recurring':
            task_id = request.POST.get('task_id')
            task_to_finish = RecurringTask.objects.get(id=task_id)
            last_event = task_to_finish.latest_event
            last_event.completed_time = datetime.now()
            last_event.save()


            new_event = RecurringEvent()
            new_event.task = task_to_finish
            new_event.task_name = task_to_finish.task_name
            new_event.started_time = datetime.now()
            new_event.completed_time = datetime.now()
            new_event.save()

            task_to_finish.latest_event = new_event
            task_to_finish.save()
        elif task_type == 'recurring_cancel':
            task_id = request.POST.get('task_id')
            task_to_finish = RecurringTask.objects.get(id=task_id)
            task_to_finish.active = False
            task_to_finish.save()

        elif task_type == 'deadline_new':
            task_name = request.POST.get('task_name')
            hard_dl = request.POST.get('hard_dl')
            soft_dl = request.POST.get('soft_dl')
            #should be in the form days:hours

            hd_days = int(hard_dl)
            sd_days = int(soft_dl)

            t_now = datetime.now()
            hdl = t_now + timedelta(days = hd_days)
            sdl = t_now + timedelta(days = sd_days)
            new_task = DeadlineTask()
            new_task.hard_deadline = hdl
            new_task.soft_deadline = sdl
            new_task.task_name = task_name 
            new_task.user = request.user
            new_task.save()
        elif task_type == 'recurring_new':
            task_name = request.POST.get('task_name')
            duration_days = int(request.POST.get('days'))
            duration_hours = int(request.POST.get('hours'))

            new_task = RecurringTask()
            new_task.user = request.user
            new_task.task_name = task_name
            new_task.frequency = timedelta(days = duration_days, hours = duration_hours)
            new_task.save()

            first_event = RecurringEvent()
            first_event.task = new_task
            first_event.task_name = new_task.task_name
            first_event.started_time = datetime.now()
            first_event.completed_time = datetime.now()
            first_event.save()
            new_task.latest_event = first_event 
            new_task.save()
            

    print('bye')
    recurring_tasks = RecurringTask.objects.filter(user=request.user)
    recurring_tasks = recurring_tasks.filter(active=True)

    deadline_tasks = DeadlineTask.objects.filter(user=request.user)
    deadline_tasks = deadline_tasks.filter(active=True)
    notes = Notes.objects.all()


    context = {
            "recurring_tasks": recurring_tasks,
            "deadline_tasks": deadline_tasks,
            "notes": notes 
    }

    return render(request, "base.html", context)


# Create your views here.
