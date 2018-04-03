from django.conf.urls import url

from main import views


urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^credit-page/$', views.credit_page, name='credit-page'),
]
