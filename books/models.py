from django.db import models
#
# # Create your models here.
#
# class BookModel(models.Model):
#     GENRE_CHOICES = (
#         ('HORROR', 'Horror'),
#         ('COMEDY', 'Comedy'),
#         ('FANTASY', 'Fantasy'),
#     )
#     image = models.ImageField(upload_to='films/', verbose_name='Загрузите фото')
#     title = models.CharField(max_length=100, verbose_name='укажите название книги')
#     description = models.TextField(verbose_name=' Укажите описание описание',blank=True)
#     price =  models.PositiveIntegerField(verbose_name="Укажите цену", default=0)
#     created_at = models.DateField(auto_now_add=True)
#     genre = models.CharField(max_length=10, choices=GENRE_CHOICES, default='HORROR',
#                              verbose_name='Выберите жанр')
#     time = models.TimeField(verbose_name='укажите время просмотра')
#     director = models.CharField(max_length=100, default='Иванов Иван')
#     trailer =models.URLField(verbose_name='укажите из YouTube')
#     def __str__(self):
#         return self.title
#     class Meta:
#         verbose_name = 'книга'
#         verbose_name_plural = 'книги'


class BookModel(models.Model):
    GENRE_CHOICES = (
        ('HORROR', 'Horror'),
        ('COMEDY', 'Comedy'),
        ('FANTASY', 'Fantasy'),
    )
    image = models.ImageField(upload_to='films/', verbose_name='Загрузите фото')
    title = models.CharField(max_length=100, verbose_name='укажите название книги')
    description = models.TextField(verbose_name=' Укажите описание описание',blank=True)
    price =  models.PositiveIntegerField(verbose_name="Укажите цену", default=0)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, default='HORROR',
                             verbose_name='Выберите жанр')
    time = models.TimeField(verbose_name='укажите время просмотра')
    director = models.CharField(max_length=100, default='Иванов Иван')
    trailer =models.URLField(verbose_name='укажите из YouTube')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'