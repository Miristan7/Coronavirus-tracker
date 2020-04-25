from django.shortcuts import render

def transmission(request):
    return render(request, 'main/transm.html')
