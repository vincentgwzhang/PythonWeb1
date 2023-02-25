from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
def index(request, name, age):
    print(request.path)
    print(request.method)
    print(request.GET)
    return HttpResponse("hello django 2" + ", name = " + name + ", age = " + str(age))

def index2(request):
    name = request.GET.get('name', '')
    age  = request.GET.get('age', '')
    return HttpResponse("hello django" + ", name = " + name + ", age = " + age)

class Message(View):
    def get(self, request):
        name = request.GET.get('name', '[default name]')
        age  = request.GET.get('age', '-1')
        return HttpResponse('Hello django, the name should be {} and age should be {}'.format(name, age))
    
    
class HTMLIndex(View):
    def get(self, request):
        return render(request, 'index.html', {'name': 'Vincent', 'age': 41})