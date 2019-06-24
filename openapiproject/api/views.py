from django.shortcuts import render
import os
import sys
import urllib.request
import json
# Create your views here.

client_id = "lxUHZ5H25TWw8S3rzg_5"
client_secret = "tnDqQX7Paa"

def search(request):
    return render(request, 'search.html')

def result(request):
    keyword = request.POST['keyword']
    encText = urllib.parse.quote("검색할 단어")
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        data = response.read().decode('utf-8')
        result = json.loads(data)#json 타입의 형식을 dict로 변경시켜준다.
        for post in result['items']:
            print('접근 성공')
            print(result['items'])
            return render(request,'result.html',{'posts': result['items']})
    return HttpResponse('API 접근불가')
