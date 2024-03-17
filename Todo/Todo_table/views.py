from django.shortcuts import render
from django.contrib import messages
from .models import Todo



# Create your views here.
def index(request):
    obj=Todo.objects.all()
    if request.POST and 'add_new' in request.POST:
       title=request.POST['title']
       description=request.POST['desc']
       type=request.POST['type']
       ins_obj=Todo.objects.create(title=title, description=description,type=type)
       ins_obj.save()
       messages.success(request, 'Todo added successfully')
       obj=Todo.objects.all()
       return  render(request, 'index.html', {'obj':obj})
    else:
        if request.POST:
            messages.error(request, 'Todo not added')
  
    return  render(request, 'index.html',{'obj':obj})

def read(request):
    return  render(request, 'result.html')

