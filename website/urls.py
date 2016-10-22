"""sds URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from views import home_page,overview_page,mission_page,vision_page,events_page,family_page,admissions_page,contact_page
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home_page),
    url(r'^overview/',overview_page),
    url(r'^mission/',mission_page),
    url(r'^vision/',vision_page),
    url(r'^gallery/',events_page),
    url(r'^team/',family_page),
    url(r'^registration/',admissions_page),

    url(r'^contact/',contact_page),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 





#url(r'^erp/',erp_page),
  
