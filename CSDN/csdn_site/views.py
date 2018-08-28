from django.shortcuts import render

# Create your views here.
from csdn_site.models import CsdnUser, Data


def user_list(request):
    # 查找所有用户
    users = CsdnUser.objects.all()
    context = {
        'users': users
    }
    return render(request, template_name='user_list.html', context=context)


def article_list(request):
    # 获取用户名
    username = request.GET.get('username')
    articles = Data.objects.filter(username=username).values('csdn_article_name').distinct()
    context = {
        'articles': articles
    }
    return render(request, template_name='article_list.html', context=context)


def readnum_list(request):
    csdn_article_name = request.GET.get('csdn_article_name')
    ret = Data.objects.filter(csdn_article_name=csdn_article_name).order_by('post_time')
    ret = ret[len(ret) - 24:len(ret)]
    # ret = [i for i in ret]
    # # TODO:取反
    # ret = reversed(ret)
    return render(request, template_name='readnum_view.html', context={'ret': ret})
