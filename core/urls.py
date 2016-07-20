from django.conf.urls import url

from . import views
from core.views import *


app_name = "core"
urlpatterns = [
    url(r'^$', views.GroupListView.as_view(), name="list"),
    url(r'^git_users/$', views.GitUserListView.as_view(), name="u_list"),
    url(r'^users_data/(?P<pk>\d+)/$', views.DataListView.as_view(), name="data_list"),
    url(r'^user_data/(?P<id>\d+)/$', views.UserDataListView.as_view(), name='user_data'),
    url(r'^add_group/$', views.CreateGroupView.as_view(), name="add"),
    url(r'^add_git_user/$', views.CreateGitUserView.as_view(), name="add_git"),
    url(r'^edit_group/(?P<pk>\d+)/$', views.UpdateGroupView.as_view(), name="group"),
    url(r'^edit_group/(?P<pk>\d+)/add-user/$', views.AddUserView.as_view(), name="add_user"),
    url(r'^edit_git_user/(?P<pk>\d+)/$', views.UpdateGitUserView.as_view(), name="git_user"),
    url(r'^delete_group/(?P<id>\d+)/$', delete_group, name='delete_group'),
    url(r'^git_users/delete_git_user/(?P<id>\d+)/$', delete_git_user, name='delete_git_user')
]
