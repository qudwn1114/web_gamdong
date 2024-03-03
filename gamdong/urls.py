from django.urls.conf import path
from gamdong.views import HomeView, CarDetailView, contact

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('vehicle-detail/<int:pk>', CarDetailView.as_view(), name='vehicle-detail'),
    path('contact', contact)
]

