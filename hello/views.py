from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.



def helloWorld(request):
    return HttpResponse("<h1>Hello World</h1>")


def helloWorldHTML(request):
    return render(request, "hello.html", { "name": "Shashwat Sanket"})