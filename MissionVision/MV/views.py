from django.shortcuts import render

# Create your views here.
def sbc(request):
    return render (request, 'Misvis.html')
def bargraph(request):
    return render (request, 'bargraph.html')