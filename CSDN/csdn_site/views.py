from django.shortcuts import render

# Create your views here.
from csdn_site.models import CsdnUser


def user_list(request):
    # 查找所有用户
    users = CsdnUser.objects.all()
    context = {
        'users': users
    }
    return render(request, template_name='user_list.html', context=context)
