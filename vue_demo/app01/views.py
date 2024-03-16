from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def router_axios(request):
    return render(request, "router_axios.html")

def data1(request):
    return JsonResponse({
        "data":[
            {"id":1, "name": "Li Ming", "age": 11},
            {"id":2, "name": "Zhang Hua", "age": 12},
            {"id":3, "name": "Zhang He", "age": 13},
            {"id":4, "name": "Liu Liang", "age": 33}
        ]
    })