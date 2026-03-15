"""
URL configuration for QSC project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import home_redirect
from django.conf import settings
from django.conf.urls.static import static, serve
from django.views.generic import RedirectView
urlpatterns = [
    path('favicon.ico',RedirectView.as_view(url='/static/favicon.ico')),
    path('admin/', admin.site.urls),
    path('', home_redirect, name='home_redirect'),
    path('DKQSZ119/', include('DKQSZ119.urls')),
    path('D2SX/', include('D2SX.urls')),
]
urlpatterns += [
        path ('favicon.ico', serve, {
               'path' : 'favicon.ico',
              'document_root': 'static',
             }),
    ]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
