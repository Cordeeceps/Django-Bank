"""bankingsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import path, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

from core.views import home, about


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # Accounts
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # core
    path('', home, name='home'),
    path('about/', about, name='about'),
    # transactions
    path('deposit/', include('transactions.urls', namespace='transactions')),
    path('withdrawal/', include('transactions.urls', namespace='transactions')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
        )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
        )