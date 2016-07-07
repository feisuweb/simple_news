from django.conf.urls import include, url
from bbs import views

urlpatterns = [
    url(r'^index/$', views.Index),
    url(r'^regist/$', views.Regist),
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
]
