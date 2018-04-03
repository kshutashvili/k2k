from django.conf.urls import url

from finance.views import TransferView, TransferViewPage


urlpatterns = [
    url(r'^transfers/$', TransferView.as_view(), name='transfers'),
    url(r'^transfers-page/$', TransferViewPage.as_view(), name='transfers-page'),
]
