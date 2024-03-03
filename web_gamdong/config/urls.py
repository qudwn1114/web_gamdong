from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import TemplateView
from config.sitemaps import StaticViewSitemap
from gamdong.sitemaps import VehicleSitemap

sitemaps = {
    'static':StaticViewSitemap,
    'vehicle': VehicleSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt',  TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('', include('gamdong.urls')),
]