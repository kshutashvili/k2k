from django.conf.urls import url

from main import views


urlpatterns = [
    url(r'^loan/$', views.landing, name='loan'),
    url(r'^credit-page/$', views.credit_page, name='credit-page'),
]
