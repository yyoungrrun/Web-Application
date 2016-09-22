"""webapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

import grumblr.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', grumblr.views.home),
    url(r'^add-item', grumblr.views.add_item),
    url(r'^delete-item/(?P<id>\d+)$', grumblr.views.delete_item),
    # Route for built-in authentication with our own custom login page
    url(r'^login$', django.contrib.auth.views.login, {'template_name':'grumblr/login.html'}, name='login'),
    # Route to logout a user and send them back to the login page
    url(r'^logout$', django.contrib.auth.views.logout_then_login, name='logout'),
    url(r'^register$', grumblr.views.register),
]