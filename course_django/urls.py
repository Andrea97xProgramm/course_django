"""
URL configuration for course_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import (
    include,
    path,
)

from general.views import HomePageView


urlpatterns = [
    path('napshhdf/', admin.site.urls),
    path('examples/', include('examples.urls')),
]

urlpatterns += i18n_patterns(
    path('', HomePageView.as_view(), name='home'),
    path('hr/', include(('hr.urls', 'hr'), namespace='hr')),
    path('i18n/', include('django.conf.urls.i18n')),
)
