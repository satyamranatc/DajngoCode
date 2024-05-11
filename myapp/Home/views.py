from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def Home(request):
    return render(request,'Home.html')



def Data(request):
    Data = ["image.png", "image2.png"]
    return JsonResponse({"Data":Data})