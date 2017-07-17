from django.conf.urls import url
from django.contrib import admin
from gossip.views import LinkListView, LinkCreateView, LinkDetailView, LinkUpdateView, LinkDeleteView
from django.conf import settings
from django.conf.urls.static import static
from gossip import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^home/$', LinkListView.as_view(), name='home'),
    url(r'^create/$', LinkCreateView.as_view(), name='link_create'),
    url(r'^link/(?P<pk>\d+)/$', LinkDetailView.as_view(), name='link_detail'),
    url(r'^link/update/(?P<pk>\d+)/$', LinkUpdateView.as_view(), name='link_update'),
    url(r'^link/delete/(?P<pk>\d+)/$', LinkDeleteView.as_view(), name='link_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
