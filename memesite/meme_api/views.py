from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests,json
from django.template import loader

# Create your views here.

def index(request):
    url = 'https://api.imgflip.com/get_memes'
    response = requests.get(url)
    #Convers json to dict
    result = response.json()
    print(result['data'])
    template = loader.get_template('meme_api/index.html')
    return HttpResponse(template.render(result['data'],request))