from django.conf.urls import url

from csdn_site.views import user_list,article_list,readnum_list

urlpatterns = [
    url(r'^user_list/', user_list, name='user_list'),
    url(r'^article_list/', article_list, name='article_list'),
    url(r'^readnum_list/',readnum_list,name='readnum_list')
]
