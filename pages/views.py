from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): #args, keyword args
    return render(request, 'home.html', {})

def game_view(request, *args, **kwargs):
    print(request, *args, **kwargs)
    print(request.user)
    return HttpResponse("<h1>Game View</h1>") #string of html code

def user_find(request, *args, **kwargs):
    my_context={
        "game_text":"This is a game",
        "name":"sudoko",
        "size":9,
        "my_list": [123,24325,423,'abc'],
        "header":"<h1>Hello</h1>"
    }
    return render(request, 'user.html', my_context)
