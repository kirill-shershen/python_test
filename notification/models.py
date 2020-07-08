from django.db import models

class Options(models.Model):
    '''options'''
    name = models.CharField('Название', max_length=200)
    value = models.NullBooleanField('Значение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Опция'
        verbose_name_plural = 'Опции'
    
class Pushes(models.Model):
    '''pushes'''
    title = models.CharField('Заголовок уведомления', max_length=50, help_text='Укажите заголовок')
    text = models.CharField('Текст уведомления', max_length=100, help_text='Укажите текст уведомления')
    picture = models.URLField('Изображение уведомления', max_length=200, help_text='Пример: https://yourapp.com/image.png')
    date_created = models.DateField('Дата создания', auto_now_add=True)
    date_pushed = models.DateField('Дата отправки', help_text='DD/MM/YY')
    name = models.CharField('Название уведомления', max_length=100)
    count = models.PositiveIntegerField('Количество', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'