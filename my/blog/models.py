from django.db import models
from django.utils import timezone

class Category(models.Model):
    class Meta():
        db_table = 'category'
        ordering = ['name']

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=64, unique=True,null=True,default=None, verbose_name='Категория')
    slug = models.SlugField(verbose_name='Транслит', null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return  self.name






class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, blank=True, null=True, default=None)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='blogimage/', verbose_name=u'Ваше фото', )
    video = models.CharField(max_length=64, blank=True,default=None, verbose_name='Видео')
    is_active = models.BooleanField(default=False, verbose_name='в подвал')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return "%s,%s" % (self.id, self.title)
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'