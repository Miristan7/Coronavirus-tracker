from django.shortcuts import render

def symptoms(request):
    return render(request, 'main/sympt.html')
