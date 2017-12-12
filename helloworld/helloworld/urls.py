"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from predictions import views

from django.views.generic import View
from django.http import HttpResponse

import os

class ReactAppView(View):
    def get(self, request):
        try:

            with open(os.path.join('frontend', 'index.html')) as file:
                return HttpResponse(file.read())

        except :
            return HttpResponse(
                """
                react broken :(
                """,
                status=501,
            )


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', views.home, name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^',ReactAppView.as_view())
]
