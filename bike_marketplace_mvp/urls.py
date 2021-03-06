from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

import views


urlpatterns = patterns("",
    # url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^$", views.home, name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),

    # e.g. /bikes/1/
    url(r'^bikes/(?P<bike_id>\d+)/$', views.detail, name='detail'),

    # e.g. /search/
    url(r'^search/', views.search, name='search'),    

    # e.g. /sellers/1/
    url(r'^sellers/(?P<seller_id>\d+)/$', views.seller_detail, name='seller'),

    url(r"^about/$", TemplateView.as_view(template_name="about.html"), name="about"),

    url(r"^contact/$", TemplateView.as_view(template_name="contact.html"), name="contact"),

    url(r"^thanks/$", TemplateView.as_view(template_name="thanks.html"), name="thanks"),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
