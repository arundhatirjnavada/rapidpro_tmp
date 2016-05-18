from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import api, ApiExplorerView, AuthenticateView, BroadcastEndpoint, ChannelsEndpoint, ChannelEventsEndpoint
from .views import CampaignsEndpoint, CampaignEventsEndpoint, ContactsEndpoint, FieldsEndpoint, GroupsEndpoint
from .views import LabelsEndpoint, MediaEndpoint, MessagesEndpoint, OrgEndpoint, RunsEndpoint


urlpatterns = [
    url(r'^$', api, name='api.v2'),
    url(r'^/explorer/$', ApiExplorerView.as_view(), name='api.v2.explorer'),
    url(r'^/authenticate$', AuthenticateView.as_view(), name='api.v2.authenticate'),

    # ========== endpoints A-Z ===========
    url(r'^/broadcasts$', BroadcastEndpoint.as_view(), name='api.v2.broadcasts'),
    url(r'^/campaigns$', CampaignsEndpoint.as_view(), name='api.v2.campaigns'),
    url(r'^/campaign_events$', CampaignEventsEndpoint.as_view(), name='api.v2.campaign_events'),
    url(r'^/channels$', ChannelsEndpoint.as_view(), name='api.v2.channels'),
    url(r'^/channel_events$', ChannelEventsEndpoint.as_view(), name='api.v2.channel_events'),
    url(r'^/contacts$', ContactsEndpoint.as_view(), name='api.v2.contacts'),
    url(r'^/fields$', FieldsEndpoint.as_view(), name='api.v2.fields'),
    url(r'^/groups$', GroupsEndpoint.as_view(), name='api.v2.groups'),
    url(r'^/labels$', LabelsEndpoint.as_view(), name='api.v2.labels'),
    url(r'^/media$', MediaEndpoint.as_view(), name='api.v2.media'),
    url(r'^/messages$', MessagesEndpoint.as_view(), name='api.v2.messages'),
    url(r'^/org$', OrgEndpoint.as_view(), name='api.v2.org'),
    url(r'^/runs$', RunsEndpoint.as_view(), name='api.v2.runs'),

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
