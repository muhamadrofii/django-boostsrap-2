"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
import infoapp.views as infoapp_views  # Mengimpor views dengan alias
import contentapp.views as contentapp_views  # Mengimpor views dengan alias
import accountsapp.views as accountsapp_views  # Mengimpor views dengan alias
import subscriptionsapp.views as subscriptionsapp_views  # Mengimpor views dengan alias

# from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', infoapp_views.index, name='index'),
    path('berita/', infoapp_views.berita, name='berita'),
    path('tentangKami/', infoapp_views.tentangKami, name='tentangKami'),
    path('faq/', infoapp_views.faq, name='faq'),
    path('kids/', contentapp_views.kids, name='kids'),
    path('parents/', contentapp_views.parents, name='parents'),
    path('login/', accountsapp_views.login, name='login'),
    path('register/', accountsapp_views.register, name='register'),
    path('langganan/', subscriptionsapp_views.langganan, name='langganan'),
    path('profile/', accountsapp_views.profil, name='profil')

]
