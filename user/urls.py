from django.urls import re_path
from user import views

urlpatterns = [
    re_path(r'^register$', views.register),
    re_path(r'^user$', views.user_list),
    re_path(r'^userid/(?P<id>\d+)$', views.user_id),
    re_path(r'^profileid/(?P<id>d+)$', views.profile_id),
]