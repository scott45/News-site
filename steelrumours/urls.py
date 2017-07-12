from django.conf.urls import url
from django.contrib import admin
from gossip.views import LinkListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LinkListView.as_view(), name='home'),
]
