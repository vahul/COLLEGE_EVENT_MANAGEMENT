"""
URL configuration for event_management project.

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
from events import views as event_views
from events.views import admin_home
from django.urls import path
#from events.views import events, add_event, remove_event
from events.views import enter_event, display_events, delete_event
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', event_views.login_view, name='login'),
    path('home/', event_views.home, name='home'),
    path('about/', event_views.about, name='about'),
    path('signup/', event_views.signup_view, name='signup'),
    path('sign/', event_views.sign, name='sign'),
    path('instructionsadmin/', event_views.instructionsadmin, name='instructionsadmin'),

    path('user_form/', event_views.user_form, name='user_form'),
    path('adminlogin/',event_views.adminlogin_view,name='adminlogin'),
path('admin_home/', admin_home, name='admin_home'),
path('profile/', event_views.profile, name='profile'),
#path('registered/', event_views.registered, name='registered'),
#path('events/', events, name='events'),
    path('register_event/', event_views.register_event, name='register_event'),

                  #   path('add_event/', add_event, name='add_event'),
  #  path('remove_event/<int:event_id>/', remove_event, name='remove_event'),
    path('enter_event/', event_views.enter_event, name='save_event'),
    path('display_events/', event_views.display_events, name='display_events'),
    path('admindisplay_events/', event_views.admindisplay_events, name='admindisplay_events'),

    path('delete_event/<int:event_id>/', delete_event, name='delete_event'),
path('registered_events/', event_views.registered_events, name='registered_events'),
                  path('logged_in_users/', event_views.logged_in_users, name='logged_in_users'),
                  path('class_list/', event_views.class_list, name='class_list'),
                  path('add_class/', event_views.add_class, name='add_class'),
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
