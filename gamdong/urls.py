from django.urls.conf import path
from gamdong.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]