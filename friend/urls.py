from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from friend.views import GroupListView,GroupDetailView, search_friend, ajax_search_friend
from friend.views import friend_add_pre, ajax_friend_add_accept, ajax_friend_add_refuse, ajax_group_list


urlpatterns = patterns('',
    url(r'^$',login_required(GroupListView.as_view()),name='group_list'),
    url(r'^group/(?P<pk>\d+)/$',login_required(GroupDetailView.as_view()),name='group_detail'),
    url(r'^search/$',search_friend,name='friend_search'),
    url(r'^add/$',friend_add_pre,name='friend_add_pre'),
    url(r'^ajax_search/$',ajax_search_friend,name='ajax_friend_search'),
    url(r'^ajax_group/$',ajax_group_list,name='ajax_group_list'),
    url(r'^ajax_friend_add_refuse',ajax_friend_add_refuse,name='ajax_friend_add_refuse'),
    url(r'^ajax_friend_add_accept',ajax_friend_add_accept,name='ajax_friend_add_accept'),

)