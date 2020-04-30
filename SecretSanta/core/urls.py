"""SecretSanta URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
# from django.contrib import admin
from .views.index_view import Index_view
from .views.login_view import Login_view

urlpatterns = [
    # url(r'^polls/', include('polls.urls')),
    url(r'^$', Index_view.index, name='index'),
    url('sign_in', Login_view.sign_in, name='sign_in'),
    url('sign_out', Login_view.sign_out, name='sign_out'),
    url('create_user', Login_view.create_user, name='create_user'),
    url('create_user', Login_view.create_user, name='create_user'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # url(r'^$', views.login, name='login'),
    # url(r'^$', views.group_list, name='group_list'),
    # url(r'^$', views.logout, name='logout'),
    # url(r'^$', views.validation, name='validation'),
    # url(r'^$', views.group_creation, name='group_creation'),
    # url(r'^$', views.santa_form, name='santa_form'),
]
