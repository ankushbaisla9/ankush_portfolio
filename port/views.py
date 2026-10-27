from django.shortcuts import render,redirect
from .models import port
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method=="POST":
        port.objects.create(
            name= request.POST.get('name'),
            email= request.POST.get('email'),
            subject= request.POST.get('subject'),
            message= request.POST.get('message'),
        )
        messages.success(request,"Your Query/Message has been sent  successfully to the User!!!!!!")
        return redirect("/")
    return render(request,"home.html")