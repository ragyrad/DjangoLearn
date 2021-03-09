from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/char/room/(?P<course_id>\d+)/$', consumers.ChatConsumer),
]