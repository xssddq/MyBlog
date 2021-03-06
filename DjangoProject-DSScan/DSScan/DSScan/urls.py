"""DSScan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from sqliscan import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^task/$', views.sql_tasks, name='task'),
    url(r'^$', views.url_sql, name='home'),
    url(r'^scan/$', views.sql_scan, name='scan'),
    url(r'^vuls/$', views.vul_tasks, name='vuls'),
    url(r'^search/', views.url_search, name='search'),
    url(r'^config/$', views.scan_config, name='config'),

]
