from django.shortcuts import render,redirect
from .models import ToDo_app
from django.contrib import messages
# Create your views here.
def home(request):
    post = ToDo_app.objects.all()
    if request.method=='POST':
        #the ['content'] below is the name of the input type in HTML form
        content = request.POST['content']
        #this line of code below collects data from HTML form and saves it into the database
        Content= ToDo_app.objects.create(content=content)
        messages.success(request, 'list has been submitted')
    return render(request, 'home.html', {'post':post})


def content(request,pk):
    posts = ToDo_app.objects.get(id=pk)
    return render(request, 'content.html',{'posts':posts})

def delete(request, pk):
    #this below is the dictionary for the initial data field name as keys
    context = {'content':content}
    #this command below fetches the object related to the passed id
    DEL = ToDo_app.objects.get(id=pk)
    if request.method == 'POST':
        DEL.delete()
        return redirect("/")
    return render(request, 'home.html', context)