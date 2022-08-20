"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from pages.views import *
from blog.views import *
from sudoko.views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('home/', home_view),
    path('people_detail/', ppl_detail_view), #sss
    path('people_create/', ppl_create_view),
    path('people_create_own/', ppl_create_view_own),
    path('people_create_dj/', ppl_create_view_dj),
    path('game/', game_view),
    path('user/', user_find),
    path('admin/', admin.site.urls),
    path('people_detail/<int:my_id>/', dynamic_lookup_view, name = 'blog'),
    path('people_detail/<int:my_id>/delete/', blog_delete_view, name = 'blog delete'),
    path('sudoko/', sudoko_view),
    path('sudoko/wrong/', sudoko_wrong_view),
    path('sudoko_complete/', completed_view),
    path('sudoko/show_answer/', answer_view),
]
