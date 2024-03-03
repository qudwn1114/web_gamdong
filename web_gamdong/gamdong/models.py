from django.db import models
from django.urls import reverse


# Create your models here.
class ElectionVehicle(models.Model):
    title = models.CharField(db_column='title', max_length=255)
    description = models.TextField(db_column='description')
    path = models.CharField(db_column='path', max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성시간')

    def get_absolute_url(self):
        return reverse('vehicle-detail', kwargs={'pk': self.pk})
    
    class Meta :
        db_table = 'election_vehicle'

class ElectionVehicleDetail(models.Model):
    path = models.CharField(db_column='path', max_length=1024)
    vehicle = models.ForeignKey(ElectionVehicle, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성시간')
    
    class Meta :
        db_table = 'election_vehicle_detail'

class ElectionVehicleGallery(models.Model):
    title = models.CharField(db_column='title', max_length=255, default='')
    path = models.CharField(db_column='path', max_length=1024)
    vehicle = models.ForeignKey(ElectionVehicle, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성시간')
    
    class Meta :
        db_table = 'gallery'

class ElectionVehicleGalleryDetail(models.Model):
    path = models.CharField(db_column='path', max_length=1024)
    gallery = models.ForeignKey(ElectionVehicleGallery, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성시간')
    
    class Meta :
        db_table = 'gallery_detail'