from django.db import models
from .singleton_model import SingletonModel


class Application(models.Model):
    phone_number = models.CharField(max_length=255, verbose_name='Телефон')
    name = models.CharField(max_length=100, verbose_name='Имя')
    text = models.TextField(verbose_name='Комментарий')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.phone_number


class SiteSettings(SingletonModel):
    main_image = models.ImageField(upload_to='site_images', blank=True, null=True)
    title_main_image_1 = models.CharField(max_length=255, null=True, blank=True)
    title_main_image_2 = models.CharField(max_length=255, null=True, blank=True)
    title_about_project = models.TextField(blank=True, null=True)
    text_about_project = models.TextField(blank=True, null=True)
    count_flats = models.CharField(max_length=255, blank=True, null=True)
    about_project_image_1 = models.ImageField(upload_to='site_images', blank=True, null=True)
    about_project_image_2 = models.ImageField(upload_to='site_images', blank=True, null=True)
    about_project_image_3 = models.ImageField(upload_to='site_images', blank=True, null=True)
    architecture_title = models.TextField(null=True, blank=True)
    architecture_text = models.TextField(null=True, blank=True)
    developer_text = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Blog 1'
        verbose_name_plural = 'Blog 1'

    def __str__(self):
        return f'Blog 1'


class Layout(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    text = models.TextField()
    image = models.ImageField(upload_to='site_images')

    def __str__(self):
        return self.title
