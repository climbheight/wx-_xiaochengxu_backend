"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.conf import settings
from .views import welcome

from rest_framework.routers import SimpleRouter
from .views import BannerView,CollectionView
router = SimpleRouter()
router.register("collection",CollectionView,"collection")
router.register("banner",BannerView,"banner")
urlpatterns = [
    path("welcome/", welcome),

]
urlpatterns += router.urls
