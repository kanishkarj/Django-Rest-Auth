"""DjangoAuth URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from .views import return_token,LogOut,LogIn,Registration,home,UpdateProfile,ChangePassword
from .authAddons import activate

urlpatterns = [
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^return-token$',return_token,name="return-token"),
    url(r'^logout$',LogOut.as_view(),name="logout"),
    url(r'^login$',LogIn.as_view(),name="login"),
    url(r'^update$',UpdateProfile.as_view(),name="logout"),
    url(r'^home$',home,name="home"),
    url(r'^register$',Registration.as_view(),name="registration"),
    url(r'^passwordreset$',ChangePassword.as_view(),name="passwordreset"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='reset'),
]
