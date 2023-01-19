from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from Part2.models import Registration

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

    
   

def welcome2(request):
    return render(request,'index2.html')

def goForm2(request):
    if  request.method == "POST":
        uname = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        registration = Registration.objects.create(
            uname = uname,
            email = email,
            password = password,
            fname = fname,
            mname = mname,
            lname = lname,
            phone = phone
        )
        registration.save()
        return redirect('/Part2/welcome2/')

    return render (request,'form2.html')

def goTable2(request):
   users=Registration.objects.all()
   data={
    'users':users
   }
   return render (request, 'table2.html',data)
  
    


