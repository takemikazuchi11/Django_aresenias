from django.shortcuts import render
from django.http import HttpResponse
from Guest.models import services ,register,bookForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return HttpResponse("This is Guest Page")

def gHome(request):
    return render(request,'guessHome.html')

def gLogin(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']
        try:
            reg = register.empAuth_object.get(request, uname=uname,password=password)
            if reg is not None:
                return redirect(request,'gRegister',{})
            else:
                msg = 'Error Login'
                form = AuthenticationForm(request.POST)
                return render(request,'guessLogin.html',{'form': form, 'msg' : msg})
        except Exception as identifier:
           msg = 'Error Login'
           form = AuthenticationForm(request.POST)
           return render(request,'guessLogin.html',{'form': form, 'msg' : msg})
    else:
        form =AuthenticationForm()
        return render (request,'guessLogin.html',{'form': form})
       
        
        
   
def gRegister(request):
    if  request.method == "POST":
        uname = request.POST['uname']
        email = request.POST['email']
        password = request.POST['password']
        fname = request.POST['fname']
        lname = request.POST['lname']
        address = request.POST['address']
        phone = request.POST['phone']
        reg = register.objects.create(
            uname = uname,
            email = email,
            password = password,
            fname = fname,
            lname = lname,
            address = address,
            phone = phone
        )
        reg.save()
        messages.success(request, "Successfully Registered" )
        #return redirect('/')
    return render(request,'guessRegister.html')


def gAbout(request):
    return render(request,'guessAbout.html')

def gService(request):
    serv=services.objects.all()
    data={
        'serv':serv
    }
    return render(request,'guessService.html',data)

def gHPAge(request):
    return render(request,'guessHomePage.html')

def gBook(request):
    serv = services.objects.values_list('name',flat=True)
    

    if  request.method == "POST":
        fname = request.POST['fname']
        contactno = request.POST['contactno']
        packages = request.POST['packages']
        date = request.POST['date']
        time = request.POST['time']
        add = request.POST['add']

        book = bookForm.objects.create(
            fname = fname,
            contactno = contactno,
            packages = packages,
            date = date,
            time = time,
            add = add,
          
        )
        book.save()
        messages.success(request, "Successfully Booked an Appointment" )
    else:
        messages.success(request, "Something went wrong please try again!" )
       # return redirect('gHPage')
    return render(request,'guessBookAppoint.html', {'serv':serv})
