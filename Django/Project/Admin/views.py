from django.shortcuts import render,redirect
from django.http import HttpResponse
from Guest.models import services ,register,bookForm
from django.contrib import messages
from Guest.forms import UForm,PForm
# Create your views here.

def home(request):
    return HttpResponse("This is Admin Page")

def aHome(request):
    return render(request,'adminHome.html')

def tryy():
     return HttpResponse("This is Admin Page")

# Views for Users

def aUser(request):
    sr=register.objects.all()
    data={
        'sr':sr
    }
    return render(request,'adminUserList.html',data)




def aAppointment(request):
    return render(request,'adminAppointmentList.html')

def start(request):
    return render(request,'startPage.html')

def aUUpdate(request, id):
    user = register.objects.get(id=id)
    return render(request,'adminUUpdate.html',{'user':user})

def aUEdit(request, id):
    user = register.objects.get(id=id)
    form = UForm(request.POST, instance= user)
    if form.is_valid():
        form.save()
        #messages.success(request, "Successfully Updated" )
        return redirect("/Admin/aUser")
    else:
        messages.success(request, "Errorr" )
    return render(request,'adminUserList.html',{'user':user})

def aUDelete(request, id):
    user = register.objects.get(id=id)
    user.delete()
    return redirect("/Admin/aUser")

# Views for Packages Services

def aPackages(request):
    service=services.objects.all()
    data={
        'service':service
    }
    return render(request,'adminPackagesList.html',data)

def aPAdd(request):
    if  request.method == "POST":
        name = request.POST['name']
        discount = request.POST['discount']
        price = request.POST['price']
        details = request.POST['details']

        serv = services.objects.create(
            name = name,
            discount = discount,
            price = price,
            details = details,
        )
        serv.save()
        messages.success(request, "Successfully Add a New Product!" )
        #return redirect('/Admin/aPackages')

    return render(request,'adminPAdd.html')

def aPUpdate(request, id):
    serv = services.objects.get(id=id)
    return render(request,'adminPUpdate.html',{'serv':serv})

def aPEdit(request, id):
    serv = services.objects.get(id=id)
    form = PForm(request.POST, instance= serv)
    if form.is_valid():
        form.save()
        #messages.success(request, "Successfully Updated" )
        return redirect("/Admin/aPackages")
    else:
        messages.success(request, "Error" )
    return render(request,'adminUserList.html',{'serv':serv})

def aPDelete(request, id):
    serv = services.objects.get(id=id)
    serv.delete()
    return redirect("/Admin/aPackages")

# Views for Packages Services

def aBookForm(request):
    booked=bookForm.objects.all()
    data={
        'booked':booked
    }
    return render(request,'adminBookList.html',data)

def aBDelete(request, id):
    booked = bookForm.objects.get(id=id)
    booked.delete()
    return redirect("/Admin/aBookForm")

