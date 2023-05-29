from django.urls import path

from .views import index, todo, addTodo, editTodo, excluirTodo , toComplete

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('todo/<int:pk>', todo, name='todo'),
    path('todo/<int:pk>/edit', editTodo, name='editTodo'),
    path('todo/add', addTodo, name='addTodo'),
    path('<int:pk>', excluirTodo, name='excluirTodo'),
    path('complete/<int:pk>', toComplete, name='toComplete'),
]