from django.shortcuts import render
from django.http import HttpResponse
import json
from datetime import datetime
import random

# Create your views here.
def get_books(request):
    mybook={
        1:"java-book",
        2:"python-book",
        3:"c-book"
    }

    return HttpResponse(json.dumps(mybook))

def index(request):
    now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f'<h1>現在時刻:{now}</h1>')

def get_lottery(request):
    numbers=sorted(random.sample(range(1,50),6))
    x=random.randint(1,50)
    number_str=' '.join(map(str,numbers))
    return render(request,'lottery.html',{'numbers':number_str,'x':x})

def get_lottery2(request):
    numbers=sorted(random.sample(range(1,50),6))
    print(numbers)
    x=random.randint(1,50)
    number_str=' '.join(map(str,numbers))+f' 特別號:{x}'
    return HttpResponse('<h1>本期預測號碼:</h1>'+'<h2>'+number_str+'</h2>')

