from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

    
   

def welcome(request):
    return render(request,'index.html')

def goForm(request):
    context = {
        'Name' : 'Justin Goyena',
        'Age'  : 20,
        'Course': 'BSIT',
        'Section': '3-F2',
    }
    return render (request,'form.html',context)

def goTable(request):
    data ={
                   
                    'Prof1' : {'Juan dela Cruz',21,'IT Research Method','Teacher 1','Bansud'},
                    'Prof2'  : {'Pedro Kalungsod',22,'Event Driven','Teacher 2','Singapore'},
                    'Prof3': {'Ebang Adarna',21,'Networking 2','Teacher 4','Calapan'},
                    'Prof4': {'Toyang Calamba',27,'Application Development','Teacher 3','Mars'},
                    
                
                    
                    
             
    }
  
    return render (request, 'table.html',data)
