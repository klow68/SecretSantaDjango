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
from .views import index_view
from .views import login_view

urlpatterns = [
    # url(r'^polls/', include('polls.urls')),
    url(r'^$', index_view.index, name='home'),
    url(r'^account/', include('account.urls')),
    url('sign_in', login_view.sign_in, name='sign_in'),
    url('sign_out', login_view.sign_out, name='sign_out'),
    url('create_user', login_view.create_user, name='create_user'),
    url('create_user', login_view.create_user, name='create_user'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # url(r'^$', views.login, name='login'),
    # url(r'^$', views.group_list, name='group_list'),
    # url(r'^$', views.logout, name='logout'),
    # url(r'^$', views.validation, name='validation'),
    # url(r'^$', views.group_creation, name='group_creation'),
    # url(r'^$', views.santa_form, name='santa_form'),
]


"""
 ^account/ ^signup/$ [name='account_signup']
^account/ ^login/$ [name='account_login']
^account/ ^logout/$ [name='account_logout']
^account/ ^confirm_email/(?P<key>\w+)/$ [name='account_confirm_email']
^account/ ^password/$ [name='account_password']
^account/ ^password/reset/$ [name='account_password_reset']
^account/ ^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$ [name='account_password_reset_token']
^account/ ^settings/$ [name='account_settings']
^account/ ^delete/$ [name='account_delete'] 
"""