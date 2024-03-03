from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.views.decorators.http import require_http_methods
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
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


@require_http_methods(["POST"])
def contact(request: HttpRequest):
    '''
        메일 전송
    '''
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    to_email = 'dh1630@naver.com'

    try:
        message = render_to_string('contact_email.html', {
            'name' : name,
            'email' : email,
            'phone' : phone,
            'message' : message
        })

        mail_title = f"[Gamdong Motors] Contact 메일 ({name})"
        sendEmail = EmailMessage(mail_title, message, settings.EMAIL_HOST_USER, to=[to_email])
        sendEmail.send()
    except:
        return JsonResponse({
            'message' : '전송 에러...'
        }, status = 400)

    return JsonResponse({
        'message' : '이메일이 전송되었습니다.'
    }, status = 200)