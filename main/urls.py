from django.urls import path


from main.views import  add_item_view, todo_list_view, update_todo_view






urlpatterns = [
    path('add_item/', add_item_view, name='add'),
    path('todo_list/', todo_list_view, name='list'),
    path('update_todo/', update_todo_view, name='update'),
]
