from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend

# Create your views here.
def index(request):
    data = Friend.objects.all()
    param = {
        'title':'Hello',
        'message':'all Friends.',
        'data':data,
    }
    return render(request, 'hello/index.html',param)