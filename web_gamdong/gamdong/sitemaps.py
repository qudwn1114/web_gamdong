from django.contrib.sitemaps import Sitemap
from gamdong.models import ElectionVehicle

class VehicleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    def items(self):
        return ElectionVehicle.objects.all()
