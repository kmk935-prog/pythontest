from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend
from .forms import HelloForm

# Create your views here.
def index(request):
    data = Friend.objects.all()
    param = {
        'title':'Hello',
        'message':'all Friends.',
        'form':HelloForm,
        'data':[],
    }
    if (request.method == 'POST'):
        num=request.POST['id']
        item = Friend.objects.get(id=num)
        param['data'] = [item]
        param['form'] = HelloForm(request.POST)
    else:
        param['data'] = Friend.objects.all()
    return render(request, 'hello/index.html',param)