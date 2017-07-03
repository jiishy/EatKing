from django.conf.urls import url
from . import views,auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search$', views.search, name='search'),
    url(r'^search/([g[0-9]*]{0,1})([rc[0-9]*]{0,1})([p[0-9]*]{0,1})([s[0-9]*]{0,1})([\W\w]*)$', views.search_submit, name='search_submit'),
    url(r'^shop/([1-9][0-9]*)$',views.enter_shop,name='enter_shop'),
    url(r'^shop/([1-9][0-9]*)/comment$',views.comment,name = 'comment'),
    url(r'^shop/([1-9][0-9]*)/like_comment$',views.like_comment,name = 'like_commment'),
    url(r'^shop/([1-9][0-9]*)/unlike_comment$',views.unlike_comment,name = 'unlike_commment'),
    url(r'^shop/([1-9][0-9]*)/like_shop$', views.like_shop, name='like_shop'),
    url(r'^shop/([1-9][0-9]*)/unlike_shop$', views.unlike_shop, name='unlike_shop'),

# auth
    url(r'^login$', auth_views.login, name='login'),
    url(r'^authenticate$', auth_views.authenticate, name='authenticate'),
    url(r'^signup$', auth_views.signup, name='signup'),
    url(r'^signup/submit$', auth_views.signup_submit, name='signup-submit'),
    url(r'^logout$', auth_views.logout, name='logout'),
    url(r'^user/([1-9][0-9]*)$',auth_views.user,name = 'user'),
    url(r'^user/([1-9][0-9]*/modify)$',auth_views.modify,name = 'modify'),
    url(r'^user/([1-9][0-9]*/modify/submit)$', auth_views.modify_submit, name='modify_submit'),
]
