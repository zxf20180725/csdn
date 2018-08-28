from django.conf.urls import url

from csdn_site.views import user_list

urlpatterns = [
    url(r'^user_list/', user_list, name='user_list'),
]
