"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from django.urls import path


urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^', include('snippets.url')),
    path('admin/', admin.site.urls),
    path('v1/', include('tutorial.version')),
    # path('^auth/', include('yonghu.urls')),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
