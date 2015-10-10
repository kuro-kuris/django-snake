from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /admin/
    url(r'^admin/', include(admin.site.urls)),
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<user_id>[0-9]+)/pet/$', views.results, name='pet'),
]
