# Generated by Django 4.1.5 on 2023-01-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamlead', '0006_indexpage_image2_indexpage_image3_indexpage_text2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='list_vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.TextField(verbose_name='Название')),
                ('description1', models.TextField(verbose_name='Описание')),
                ('skills1', models.TextField(verbose_name='Навыки')),
                ('company1', models.TextField(verbose_name='Компания')),
                ('money1', models.TextField(verbose_name='Оклад')),
                ('region1', models.TextField(verbose_name='Регион')),
                ('date1', models.DateField()),
                ('name2', models.TextField(verbose_name='Название')),
                ('name3', models.TextField(verbose_name='Название')),
                ('name4', models.TextField(verbose_name='Название')),
                ('name5', models.TextField(verbose_name='Название')),
                ('name6', models.TextField(verbose_name='Название')),
                ('name7', models.TextField(verbose_name='Название')),
                ('name8', models.TextField(verbose_name='Название')),
                ('name9', models.TextField(verbose_name='Название')),
                ('name10', models.TextField(verbose_name='Название')),
            ],
        ),
    ]
