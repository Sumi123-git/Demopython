from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class Taskview(ListView):
    model=task
    template_name = 'home.html'
    context_object_name = 'task1'

class Taskdetailview(DetailView):
    model = task
    template_name = 'detials.html'
    context_object_name = 'task2'

class Taskupdateview(UpdateView):
        model = task
        template_name = 'update.html'
        context_object_name = 'task3'
        fields = ('name','priority','date')

        def get_success_url(self):
            return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
            model = task
            template_name = 'delete.html'
            success_url = reverse_lazy('cbvhome')


# # Create your views here.
def todoadd(request):
    task1 = task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        as1 = task(name=name, priority=priority, date=date)
        as1.save()
    return render(request, "home.html", {'task1': task1})


# def detials(request):
#
#     return render(request,'detials.html',)
def delete(request, id):
    ttask = task.objects.get(id=id)
    if request.method == "POST":
        ttask.delete()
        return redirect('/')
    return render(request, "delete.html")


def update(request,id):
    taask = task.objects.get(id=id)
    form1 = TodoForm(request.POST or None, instance=taask)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request, "edit.html", {'form1': form1, 'ttask': taask})
