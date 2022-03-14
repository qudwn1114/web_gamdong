from django.urls.conf import path
from django.views.generic import TemplateView
from gamdong.views import HomeView, CarDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('vehicle-detail/<int:pk>', CarDetailView.as_view(), name='vehicle-detail'),
    path('robots.txt',  TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
]