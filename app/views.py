from django.shortcuts import render

# Create your views here.
def boy(request):
    return render(request,'boy.html')

def anil(request):
    return render(request,'anil.html')