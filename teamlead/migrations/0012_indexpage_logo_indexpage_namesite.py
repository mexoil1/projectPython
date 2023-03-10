# Generated by Django 4.1.5 on 2023-01-14 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamlead', '0011_delete_headeradm_demandad_logo_demandad_namesite_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpage',
            name='logo',
            field=models.ImageField(blank=True, upload_to='header/', verbose_name='Логотип'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='nameSite',
            field=models.TextField(default=1, verbose_name='Название сайта'),
            preserve_default=False,
        ),
    ]
