from django.http   import HttpResponse
from   django.shortcuts import  render


def home(request):
    # return HttpResponse('Hello This My Home Responsive Django Page!')
    return  render(request,'website/index.html')

# About
def about(request):
   return   render(request,"website/About.html")
# Services
def Services(request):
    return   render(request,"website/Services.html")