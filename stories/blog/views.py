from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    return render(request,'blog\home.html')
    #return HttpResponse("Hi , you'are going good.Keep moving")