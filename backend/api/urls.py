"""
URL configuration for api project.

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
from django.contrib import admin
from django.urls import re_path
from api import views

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('canteens/$', views.canteen_list),
    re_path('canteens/(?P<id>\w*)', views.canteen_detail),

    re_path('menus/$', views.menu_list),
    re_path('menus/(?P<id>\w*)$', views.menu_detail),
    re_path('menus/available/(?P<menu_id>\w*)$', views.menu_add_available),
    re_path('menus/unavailable/(?P<menu_id>\w*)$', views.menu_add_unavailable),
    re_path('menus/(?P<canteen_id>\w*)/(?P<date>.*)$', views.menu_by_canteen_by_date),

    re_path('ratings/$', views.rating_list),
    re_path('ratings/(?P<menu_id>\w*)', views.ratings_by_menu),
]
