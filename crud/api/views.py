from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import Entry


# Create your views here.
def home(request):
    return render(request , 'app/home.html')

def show(request):
    data = Entry.objects.all()
    return render(request , 'app/show.html',{'data':data})

def send(request):
    if request.method == 'POST':
        ID = request.POST['id']
        data1 = request.POST['data1']
        data2 = request.POST['data2']
        
        Entry(ID = ID , data1 = data1 , data2 = data2).save()
        msg = "Data Store Successfully"
        return render(request ,'app/home.html',{'msg':msg})
    else:
        return HttpResponse("<h1>404 - not found</h1>")
    
def delete(request):
    ID = request.GET['id']
    Entry.objects.filter(ID=ID).delete()
    return HttpResponseRedirect('show')

def edit(request):
    ID = request.GET['id']
    data1 = data2 = "Not Available"
    for data in Entry.objects.filter(ID = ID):
        data1 = data.data1
        data2 = data.data2
    return render(request,"app/edit.html" , {'ID':ID , 'data1':data1 , 'data2':data2})

def RecordEdited(request):
    if request.method == 'POST':
        ID = request.POST['id']
        data1 = request.POST['data1']
        data2 = request.POST['data2']
        Entry.objects.filter(ID = ID).update(data1 = data1 , data2 = data2)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h2>404 - Not Found</h2>")

