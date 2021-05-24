from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Post

# Create your views here.



def helloWorld(request):
    return HttpResponse("<h1>Hello World</h1>")


def helloWorldHTML(request):
    # db actions
    return render(request, "home.html", { "name": "Shashwat Sanket"})

def contactUs(request):
    posts = Post.objects.all()
    return render(request, "contact.html", {"posts": posts})