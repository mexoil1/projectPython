# Generated by Django 4.1.5 on 2023-01-14 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamlead', '0008_demand_geography_headeradm_latest_skills_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headeradm',
            name='logo',
            field=models.ImageField(blank=True, upload_to='header/', verbose_name='Логотип'),
        ),
    ]
