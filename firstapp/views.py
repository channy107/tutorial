from django.shortcuts import render
from django.http import HttpResponse
from .models import Curriculum

def index1(request):
    return HttpResponse('<h1>Hello</h1>')

def index2(request):
    return HttpResponse('<h1>Hi</h1>')

def main(request):
    return HttpResponse('<h1>Main</h1>')

def show(request):
    curriculum = Curriculum.objects.all()
    html = ''
    for cur in curriculum:
        html += cur.name

    # return HttpResponse(html)
    #             request   template              model
    return render(request, 'firstapp/show.html', {'curriculum':curriculum})