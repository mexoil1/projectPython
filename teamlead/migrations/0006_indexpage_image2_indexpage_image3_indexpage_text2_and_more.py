# Generated by Django 4.1.5 on 2023-01-13 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamlead', '0005_remove_indexpage_img_indexpage_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpage',
            name='image2',
            field=models.ImageField(blank=True, upload_to='teamlead/', verbose_name='Картинка 2'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='image3',
            field=models.ImageField(blank=True, upload_to='teamlead/', verbose_name='Картинка 3'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='text2',
            field=models.TextField(default=1, verbose_name='Второй абзац'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpage',
            name='text3',
            field=models.TextField(default=1, verbose_name='Третий абзац'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpage',
            name='text4',
            field=models.TextField(default=1, verbose_name='Четвертый абзац'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='image1',
            field=models.ImageField(blank=True, upload_to='teamlead/', verbose_name='Картинка 1'),
        ),
        migrations.AlterField(
            model_name='indexpage',
            name='text1',
            field=models.TextField(verbose_name='Первый абзац'),
        ),
    ]