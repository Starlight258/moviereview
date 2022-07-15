from django.shortcuts import render
import requests
import json
from .forms import SearchForm

my_id ='69de8325498a7bdbd3bd90ee67a6b14b' #api key
# Create your views here.
def home(request):
    if request.method == 'POST': #검색창 누르면
        form = SearchForm(request.POST) #폼
        searchword = request.POST.get('search') #검색어
        if form.is_valid(): #폼이 유효하면
            url = 'https://api.themoviedb.org/3/search/movie?api_key='+my_id+'&query='+searchword
            response = requests.get(url)
            resdata = response.text #응답 데이터
            obj = json.loads(resdata) #json 형식
            obj = obj['results']
            return render(request, 'search.html', {'obj':obj})
        # 입력된 내용을 바탕으로 
        # https://api.themoviedb.org/3/search/movie?api_key=69de8325498a7bdbd3bd90ee67a6b14b&language=en-US&query=hello&page=1&include_adult=false 
        #위 형태의 url로 get 요청 보내기
    else :
        form = SearchForm()
        url = 'https://api.themoviedb.org/3/trending/movie/week?api_key='+my_id 
        response = requests.get(url) #응답객체
        resdata = response.text #정보
        obj = json.loads(resdata) #json 형태로 정보 정리
        obj = obj['results']
    return render(request, 'index.html', {'obj':obj, 'form':form})

def detail(request, movie_id):
    url = 'https://api.themoviedb.org/3/movie/'+movie_id+'?api_key='+my_id 
    response = requests.get(url) 
    resdata = response.text 
    return  render(request, 'detail.html', {'resdata':resdata})