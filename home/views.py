from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Todo
from .forms import PostCreateForm, PostUpdateForm
# Create your views here.


def home(request):
    post=Todo.objects.all()
    return render(request,'home.html',{'context':post})

def detail(request,id):
    post=Todo.objects.get(id=id)
    return render(request,'detail.html',{'context':post})

def delete(request,id):
    Todo.objects.get(id=id).delete()
    messages.success(request,'post deleted successfully !!!')
    return render(request,'delete.html')
    # return redirect(request,'home')

def create(request):
    if request.method=='POST':
        form= PostCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'],body=cd['body'],publish=cd['publish'])
            messages.success(request,'sueccessfully...','success')
            return redirect('home')
    else:
        form = PostCreateForm()
    return render(request,'createform.html',{'form':form})

def update(request,id):
    todo=Todo.objects.get(id =id)
    if request.method == 'POST':
        form =PostUpdateForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Post Updated...','success')
            return redirect('detail',id)
        pass 
    else:
        form = PostUpdateForm(instance=todo)
    return render(request,'update.html',{'form':form})