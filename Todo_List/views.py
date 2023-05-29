from django.shortcuts import render, redirect
# from django.template import loader, Context
from django.shortcuts import get_object_or_404
from .forms import newTodo
from django.views.generic import ListView, DetailView, DeleteView, UpdateView 
from .models import Todo


class index(ListView):
    model = Todo
    template_name = 'index.html'
    context_object_name = 'todo_list'
    
    def get_queryset(self):
        return Todo.objects.all()
    
    # def get_context_data(self, **kwargs):
    #     context = super(Todo, self).get_context_data(**kwargs)
    #     context['todo_list'] = Todo.objects.all()
    #     return context

        
        
# def index(request):
#     context = {'todo_list' : Todo.objects.all()}
#     return render(request, 'index.html', context)

def todo(request, pk):
    if str(request.user) != 'AnonymousUser':
    
        todo = get_object_or_404(Todo, pk=pk)
        context = {'todo' : todo}
        return render(request, 'todo.html', context)
    else:
        return redirect(index)
    
def addTodo(request):
    if str(request.user) != 'AnonymousUser':
        if request.method == 'POST':
            new_todo = newTodo(request.POST)
            if new_todo.is_valid():
                new_todo.save()
                return redirect(index)               
        return render(request, 'addTodo.html')
    else:
        return redirect(index)

def editTodo(request, pk):
    if str(request.user) != 'AnonymousUser':
        todo = Todo.objects.get(id=pk)
        context = {'todo': todo}
        print(todo)
        if request.method == 'POST':
            form = newTodo(request.POST, instance=todo)
            if form.is_valid():
                form.save()
                return redirect(index)
        return render(request, 'editTodo.html', context)
    else:
        return redirect(index)
def excluirTodo(request, pk):
    if str(request.user)!= 'AnonymousUser':
        todo = Todo.objects.get(id=pk)
        print(todo.completed)
        todo.delete()
        return redirect(index)
    else:
        return redirect(index)
    
def toComplete(request, pk):
    if str(request.user)!= 'AnonymousUser':
        if request.method == 'POST':
            todo = Todo.objects.get(id=pk)
            todo.update_status(True)
            print(f'status: {todo.completed}')
            
            return redirect(index)
    else:
        return redirect(index)
