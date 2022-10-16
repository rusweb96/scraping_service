from django.db import models

from .utils import from_cyrillic_to_eng


class City(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Названия города',
                            unique=True)

    slug = models.CharField(max_length=50, blank=True,
                            unique=True)

    class Meta:
        verbose_name = 'Названия города'
        verbose_name_plural = 'Название городов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))

        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Язык програмирование',
                            unique=True)

    slug = models.CharField(max_length=50, blank=True,
                            unique=True)

    class Meta:
        verbose_name = 'Язык програмирование'
        verbose_name_plural = 'Языки програмирования'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))

        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True, )
    title = models.CharField(max_length=250, verbose_name='Заголовок вакансии')
    company = models.CharField(max_length=250, verbose_name='Компания')
    description = models.TextField(verbose_name='Описание вакансии')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    language = models.ForeignKey('Language', on_delete=models.CASCADE,verbose_name='Язык програмирование')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title
