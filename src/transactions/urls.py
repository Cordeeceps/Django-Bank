from django.urls import path

from .views import deposit_view, withdrawal_view


app_name = 'transactions'

urlpatterns = [
    #path(r'^$', home_view, name='home'),
    path(r'^deposit/$', deposit_view, name='deposit'),
    path(r'^withdrawal/$', withdrawal_view, name='withdrawal'),
]
