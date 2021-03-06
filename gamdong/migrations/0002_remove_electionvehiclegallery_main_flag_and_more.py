# Generated by Django 4.0.2 on 2022-03-09 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamdong', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electionvehiclegallery',
            name='main_flag',
        ),
        migrations.AlterModelTable(
            name='electionvehiclegallery',
            table='gallery',
        ),
        migrations.CreateModel(
            name='ElectionVehicleGalleryDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(db_column='path', max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamdong.electionvehiclegallery')),
            ],
            options={
                'db_table': 'gallery_detail',
            },
        ),
    ]
