from django.conf.urls import patterns, url

from ladder import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^list/$', views.list_rounds, name='list'),
                       # ex: /2013/round/1/
                       url(r'^(?P<year>\d+)/round/(?P<season_round>\d+)/$', views.season, name='season'),
                       # ex: /2013/round/1/division/1-n
                       url(r'^(?P<year>\d+)/round/(?P<season_round>\d+)/division/(?P<division_id>\d+)/$', views.ladder, name='ladder'),
                       # ex: /2013/round/1/division/1-n/add/
                       url(r'^(?P<year>\d+)/round/(?P<season_round>\d+)/division/(?P<division_id>\d+)/add/$', views.add, name='add'),
                       # ex: /player/1/
                       url(r'^player/(?P<player_id>\d+)/$', views.player_history, name='player_history'),
                       # ex: /player/
                       url(r'^player/search/$', views.player_search, name='player_search'),
                       url(r'^player/results/$', views.player_result, name='player_result'),
                       url(r'^season/ajax/stats/$', views.season_ajax_stats, name='season_ajax_stats'),

                       url(r'^add_result/(?P<ladder_id>\d+)$', views.add_result, name='add_result'),
)
