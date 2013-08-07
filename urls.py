from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'lunch.views.index'),
    url(r'^generate', 'lunch.views.ajax_generate'),
    url(r'^choose-restaurant', 'lunch.views.choose_restaurant'),
    url(r'^group/(?P<code>\w+)', 'lunch.views.html_group_page', name='group_page'),
    url(r'^show-groups/(?P<group_codes>[\w|]+)', 'lunch.views.generated_groups'),
    url(r'^admin/', include(admin.site.urls)),
)
