from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^page/$', views.chat_display, name='chat_display'),
    url(r'^create/$', views.create_chat, name='create_chat'),
]