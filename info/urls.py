from django.conf.urls import url

from info import views


urlpatterns = [
    url(r'^ask-question/$', views.ask_question, name='ask-question'),
    url(r'^(?P<slug>[\w\d][-\w\d]*)/$', views.flatpage, name='flatpage'),
]
