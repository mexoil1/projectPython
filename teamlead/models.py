from django.db import models

class indexPage(models.Model):
    name = models.TextField('Заголовок')
    text1 = models.TextField("Первый абзац")
    image1 = models.ImageField(
        'Картинка 1',
        upload_to='teamlead/',
        blank=True
    )
    text2 = models.TextField("Второй абзац")
    image2 = models.ImageField(
        'Картинка 2',
        upload_to='teamlead/',
        blank=True
    )
    text3 = models.TextField("Третий абзац")
    image3 = models.ImageField(
        'Картинка 3',
        upload_to='teamlead/',
        blank=True
    )
    text4 = models.TextField("Четвертый абзац")
    
    
class demandAd(models.Model):
    name = models.TextField('Заголовок')
    
    
class geographyAd(models.Model):
    name = models.TextField('Заголовок')
    
    
class skillsAd(models.Model):
    name = models.TextField('Заголовок')
    
    
class latestAd(models.Model):
    name = models.TextField('Заголовок')
    
    

    





