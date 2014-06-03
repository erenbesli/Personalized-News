from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'NewsRecommendation.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^login/$','NewsRec.views.LoginRequest'),
    (r'^profile/$','NewsRec.views.Profile'),
    (r'^register/$', 'NewsRec.views.ReaderRegistration'),
    (r'^news/$', 'NewsRec.views.all_news'),
    (r'^click/(?P<user_id>.*)/(?P<news_id>.*)/$','NewsRec.views.click'),
    (r'^logout/$', 'NewsRec.views.LogoutRequest'),
    (r'^userBasedRecedNews/$', 'NewsRec.views.read_userBasedRecedNews'),
    (r'^itemBasedRecedNews/$', 'NewsRec.views.read_itemBasedRecedNews'),
    (r'^HealthNews/$', 'NewsRec.views.health_news'),
    (r'^SportNews/$', 'NewsRec.views.sport_news'),
    (r'^MusicNews/$', 'NewsRec.views.music_news'),
    (r'^WorldNews/$', 'NewsRec.views.world_news'),
    (r'^MoviesNews/$', 'NewsRec.views.movies_news'),

)
