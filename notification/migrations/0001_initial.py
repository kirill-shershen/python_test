# Generated by Django 3.0.8 on 2020-07-06 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('value', models.NullBooleanField(verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Опция',
                'verbose_name_plural': 'Опции',
            },
        ),
        migrations.CreateModel(
            name='Pushes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Укажите заголовок', max_length=50, verbose_name='Заголовок уведомления')),
                ('text', models.CharField(help_text='Укажите текст уведомления', max_length=100, verbose_name='Текст уведомления')),
                ('picture', models.ImageField(help_text='Пример: https://yourapp.com/image.png', upload_to='', verbose_name='Изображение уведомления')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_pushed', models.DateField(help_text='DD/MM/YYYY', verbose_name='Дата отправки')),
                ('name', models.CharField(max_length=100, verbose_name='Название уведомления')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления',
            },
        ),
    ]
