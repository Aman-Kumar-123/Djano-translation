from django.http import HttpResponse
from django.shortcuts import render
from googletrans import Translator

T=Translator()

def index(request):
    text=request.GET.get('text1','OUTPUT TEXT')
    if(text is not 'OUTPUT TEXT'):
        text=T.translate(text,dest='hi',src='en').text
    print(text)
    params={'textarea':text}
    return render(request,'index.html',params)