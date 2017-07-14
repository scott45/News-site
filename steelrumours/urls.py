from django.conf.urls import url
from django.contrib import admin
from gossip.views import LinkListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LinkListView.as_view(), name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'login.html'}, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        name="logout"),
]
