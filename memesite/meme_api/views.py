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
    template = loader.get_template('meme_api/index.html')
    return HttpResponse(template.render(result['data'],request))



def search(request):
    url = 'https://api.imgflip.com/get_memes'
    response = requests.get(url)
    
    search = request.POST['searchVal']
    res = json.loads(response.text)
    arr1 = res.get('data').get('memes')
    meme = []
    result={}
    result['searchVal']=search
    for lists in arr1:
        if search in lists['name']:
                meme.append(lists)
                
    if(meme):
        result['memes']=meme
    
        
    print(result)
    template = loader.get_template('meme_api/index.html')
    return HttpResponse(template.render(result,request))