# Generated by Django 2.2.16 on 2020-10-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=254, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=254, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=254, null=True, verbose_name='Отчество')),
                ('deck', models.TextField(default='Если вы хотите узнать меня получше, звоните на мой номер или пишите на электронную почту)', max_length=5000, verbose_name='Описание')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('phone', models.CharField(max_length=254, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('social_page_networks', models.CharField(blank=True, max_length=254, null=True, verbose_name='Страница в соц. сети')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
