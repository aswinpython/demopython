from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from theppapp.models import Cheat

from.forms import Todo
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
# Create your views here.
class Cheatdeleteview(DeleteView):
    model = Cheat
    template_name = 'delete.html'
    success_url =reverse_lazy('cbvlistview')
class Cheatupdateview(UpdateView):
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

    model = Cheat
    template_name = 'update.html'
    context_object_name = 'cheat'
    fields = ('name','priority','date')

class Cheatlistview(ListView):
    model = Cheat
    template_name = 'home.html'
    context_object_name = 'cheat1'
class Cheatdetailview(DetailView):
    model = Cheat
    template_name = 'details.html'
    context_object_name = 'cheat'



def add(request):
    cheat = Cheat.objects.all()
    if request.method=="POST":
        name= request.POST.get('cheat','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        cheat1=Cheat(name=name,priority=priority,date=date)
        cheat1.save()
    return render(request,'home.html',{'cheat1':cheat})
def delete(request,cheat_id):
    cheat = Cheat.objects.get(id=cheat_id)
    if request.method=="POST":

        cheat.delete()
        return redirect('/')

    return render(request,'delete.html')
def update(request,id):
    cheat=Cheat.objects.get(id=id)
    f=Todo(request.POST or None,instance=cheat)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'cheat':cheat})

