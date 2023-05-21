from django.shortcuts import render,redirect#
from django.http import HttpResponse #answer text
from myapp.models import Task
from django.contrib import messages
# Create your views here.

def index(request):
     all_task = Task.objects.all()#all_person keep the data
     return render(request,"index.html",{"all_task":all_task})#---------show database

def ADD_list(request):
     if request.method == "POST":#check ข้อมูลที่ได้รับว่าเป็นpost
          #get data
          Topic = request.POST["Topic"]
          Detail = request.POST["Detail"]
          #save data
          task = Task.objects.create(
               Topic = Topic,#field=data of input
               Detail=Detail
          )
          task.save()#database
          messages.success(request,"save success")#sent messages to "/"
          #path
          return redirect("/")#save then return to frist page
     else:
          print("NO post")
     return render(request,"ADD.html")#the web


def edit(request,task_id):#with parameter
     if request.method == "POST":#check ว่ามีข้อมูลส่งมามั้ย
          task = Task.objects.get(id=task_id)#person คือข้อมูลที่เปลี่ยนแปลงเก็บในperson
          task.Topic=request.POST["Topic"]#เปลี่ยนชื่อใหม่ตามrequest.POST["name"]ตามที่updateมา
          task.Detail=request.POST["Detail"]
          task.save()
          messages.success(request,"update success")#sent messages to "/"
          #path
          return redirect("/")#save then return to frist page
     else:#ถ้าไม่มีให้ดึงข้อมูลที่จะแก้ไขมาโชว์
          #ดึงข้อมูลที่จะแก้ไข
          task = Task.objects.get(id=task_id)
     return render(request,"edit.html",{"task":task})#ส่งข้อมูล


def delete(request,task_id):#with parameter
     task = Task.objects.get(id=task_id)
     task.delete()
     messages.success(request,"delete success")#sent messages to "/"
     #path
     return redirect("/")#save then return to frist page