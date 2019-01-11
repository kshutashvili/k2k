from django.conf.urls import url

from finance.views import TransferView, TransferViewPage


urlpatterns = [
    url(r'^$', TransferView.as_view(), name='landing'),
    url(
        r'^transfers-page/$',
        TransferViewPage.as_view(),
        name='transfers-page'
    ),
]
