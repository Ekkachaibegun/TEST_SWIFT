from django.urls import path
from myapp import views#get function form "myapp_name category views"



urlpatterns = [
    path('',views.index),#''->frist page////call function "index" in views
    path('ADD',views.ADD_list),#''->form page////call function "form" in views
    path('edit/<task_id>',views.edit),#sent <value>
    path('delete/<task_id>',views.delete)#sent <value>
]