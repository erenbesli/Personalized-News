import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from NewsRec.forms import LoginForm, RegistrationForm

# Create your views here.
from django.template import RequestContext
from NewsRec.models import Reader,News, Clicks, RecedNews


def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            reader = authenticate(username=username, password=password)
            if reader is not None:
                login(request, reader)
                return HttpResponseRedirect('/profile/')
            else:
                return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))

        else:
            return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))

    else:
        ''' User is not submitting the form redirect to login form  '''
        form = LoginForm()
        context = {'form': form}
        return render_to_response('login.html', context, context_instance=RequestContext(request))


@login_required
def Profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    swapper= request.user.get_profile
    context={'swapper':swapper}
    return render_to_response('profile.html',context,context_instance=RequestContext(request))


def ReaderRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            user.save()
            #swapper = user.get_profile()
            #swapper.name = form.cleaned_data['name']
            #swapper.address = form.cleaned_data['address']
            #swapper.save()
            reader= Reader(user=user,name=form.cleaned_data['username'],slug=form.cleaned_data['slug'])
            reader.save()
            return HttpResponseRedirect('/profile/')
        else:
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
    else:
        '''user is not submitting the form show them a blank registration form'''
        form=RegistrationForm()
        context={'form':form}
        return render_to_response('register.html', context, context_instance=RequestContext(request))


def all_news(request):
    items = News.objects.all()
    context = {'items': items}
    return render_to_response('all_news.html', context, context_instance=RequestContext(request))


def health_news(request):
    items = News.objects.filter(genre="Health")
    context = {'items': items}
    return render_to_response('health_news.html', context, context_instance=RequestContext(request))

def movies_news(request):
    items = News.objects.filter(genre="Movies")
    context = {'items': items}
    return render_to_response('movies_news.html', context, context_instance=RequestContext(request))

def sport_news(request):
    items = News.objects.filter(genre="Other Sports")
    context = {'items': items}
    return render_to_response('sport_news.html', context, context_instance=RequestContext(request))

def music_news(request):
    items = News.objects.filter(genre="Music")
    context = {'items': items}
    return render_to_response('music_news.html', context, context_instance=RequestContext(request))

def world_news(request):
    items = News.objects.filter(genre="World News")
    context = {'items': items}
    return render_to_response('world_news.html', context, context_instance=RequestContext(request))




def click(request,user_id,news_id):
    click=Clicks(user_id=user_id,news_id=news_id,date=datetime.datetime.today())
    news_link=News.objects.get(id=news_id).link
    click.save()
    print(news_link)
    return HttpResponseRedirect(news_link)


def LogoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/login')


def read_userBasedRecedNews(request):
    news_list=[]
    with open('NewsRec/userBasedRecedNews.txt') as f:
        for columns in ( raw.strip().split() for raw in f ):
            recednew = RecedNews(News.objects.get(id=columns[0]).id, News.objects.get(id=columns[0]).link,News.objects.get(id=columns[0]).title,columns[1],News.objects.get(id=columns[0]).genre)
            news_list.append(recednew)
            if 'str' in columns[0]:
              break
    context = {'news_list': news_list}
    return render_to_response("userBasedRecedNews.html",context,context_instance=RequestContext(request))

def __datetime(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')


def read_itemBasedRecedNews(request):
    news_list=[]

    with open('NewsRec/itemBasedRecedNews.txt') as f:
        for columns in ( raw.strip().split() for raw in f ):
            news_date = News.objects.get(id=columns[0]).date
            news_date=datetime.datetime.strptime(news_date, '%Y-%m-%d %H:%M:%S')
            #today=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            #today = datetime.datetime.now()
            today= '2008-11-13 16:05:15'
            #today=datetime.datetime.strftime(today,'%Y-%m-%d %H:%M:%S')
            today=datetime.datetime.strptime(today,'%Y-%m-%d %H:%M:%S')
            result=(today-news_date)
            result= '%.15f' % float(1/float(result.days)*10000)
            #diff=abs((today.date()-news_date).days)
            #recency=
            alpha=0.1
            result=alpha*float(result)+(1-alpha)
            recednew = RecedNews(News.objects.get(id=columns[0]).id, News.objects.get(id=columns[0]).link,News.objects.get(id=columns[0]).title,result,News.objects.get(id=columns[0]).genre)
            news_list.append(recednew)
            if 'str' in columns[0]:
              break
    news_list_sorted=sorted(news_list, key=lambda recednew: recednew.value, reverse=True)
    context = {'news_list_sorted': news_list_sorted}
    return render_to_response("itemBasedRecedNews.html",context,context_instance=RequestContext(request))
