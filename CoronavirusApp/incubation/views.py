from django.shortcuts import render

def incubation(request):
    return render(request, 'main/incub.html')
