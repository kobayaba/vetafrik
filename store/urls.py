from django.conf.urls import url
from django.urls import path
from . import views
app_name='store'

urlpatterns = [
    url(r'^$', views.listing, name='listing'),
    path('<int:album_id>/',views.detail,name='detail'),
    #url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),
]