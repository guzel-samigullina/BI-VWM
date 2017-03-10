from django.conf.urls import url
from . import views

app_name = 'search'

urlpatterns = [
    # /search/
    url(r'^$', views.index, name='index'),

    # /search/id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /search/add_article/
    url(r'add_item/$', views.ItemCreate.as_view(), name='item-add'),

    # /search/crawler/
    url(r'crawler/$', views.crawler, name='crawler'),
]
