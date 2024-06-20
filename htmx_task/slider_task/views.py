from django.shortcuts import render
from django.http import JsonResponse

def index(req):

    return render(req, 'slider_task/index.html')


def get_temperature(req):

    temperature = int(req.POST.get('vol'))

    weather = 'hot' if temperature > 25 else 'cold'

    context = {'temperature': temperature, 'weather': weather}

    return render(req, 'slider_task/parendiv.html',context=context)



def get_text(req):

    return render(req, 'slider_task/editableform.html')



def save_text(request):

    if request.method == 'POST':

        new_text = request.POST.get('new_text')  

    return render(request, 'slider_task/h1.html',{'text': new_text}) 