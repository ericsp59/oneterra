from django.shortcuts import render

# Create your views here.

def react_app(request):
    return render(request, './reactApp/index.html')