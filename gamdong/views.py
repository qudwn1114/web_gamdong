from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from gamdong.models import ElectionVehicle, ElectionVehicleDetail, ElectionVehicleGallery, ElectionVehicleGalleryDetail
# Create your views here.

class HomeView(View):
    def get(self, request: HttpRequest): 
        context={}
        vehicle = ElectionVehicle.objects.all()
        context['vehicle'] = vehicle

        return render(request, 'index.html', context)


class CarDetailView(View):
    def get(self, request: HttpRequest, pk):
        context={}
        vehicle = get_object_or_404(ElectionVehicle, pk=pk)
        detail = ElectionVehicleDetail.objects.filter(vehicle=vehicle)
        gallery = ElectionVehicleGallery.objects.filter(vehicle=vehicle)
        context['vehicle'] = vehicle
        context['detail'] = detail
        context['gallery'] = gallery

        select_obj = self.request.GET.get('select_obj', '')
        if select_obj:
            obj = ElectionVehicleGallery.objects.get(id=select_obj)
            gallery_detail = ElectionVehicleGalleryDetail.objects.filter(gallery=obj)
            context['select_obj'] = obj
            context['gallery_detail'] = gallery_detail

        return render(request, 'car_detail.html', context)
