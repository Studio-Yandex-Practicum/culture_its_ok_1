# Generated by Django 3.2 on 2023-08-20 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('author', models.CharField(blank=True, max_length=255, null=True, verbose_name='Автор')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('how_to_get', models.TextField(blank=True, null=True, verbose_name='Как добраться')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('photo', models.ImageField(upload_to='photos', verbose_name='Обложка')),
                ('description', models.TextField(verbose_name='Описание')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес начала')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршруты',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('text', 'Текст'), ('photo', 'Фото'), ('reflection', 'Рефлексия'), ('continue_button', 'Кнопки')], max_length=20, verbose_name='Тип шага')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Текстовое содержимое')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='Фотография')),
                ('delay_after_display', models.IntegerField(verbose_name='Задержка после показа')),
            ],
            options={
                'verbose_name': 'Шаг',
                'verbose_name_plural': 'Шаги',
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('age', models.IntegerField(verbose_name='Возраст')),
            ],
        ),
        migrations.CreateModel(
            name='RouteObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_priority', models.IntegerField(verbose_name='Приоритет объекта')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture.object', verbose_name='Объект')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture.route', verbose_name='Маршрут')),
            ],
            options={
                'ordering': ('object_priority',),
            },
        ),
        migrations.CreateModel(
            name='Reflection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос бота')),
                ('answer_type', models.CharField(choices=[('text', 'Текст'), ('voice', 'Голос')], max_length=10, verbose_name='Тип ответа')),
                ('answer_content', models.TextField(verbose_name='Содержимое ответа')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture.object', verbose_name='Объект')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture.route', verbose_name='Маршрут')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture.user', verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField(auto_now_add=True, verbose_name='Время начала')),
                ('finished_at', models.DateTimeField(blank=True, null=True, verbose_name='Время окончания')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture.object', verbose_name='Объект')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture.route', verbose_name='Маршрут')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture.user', verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='ObjectStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_priority', models.IntegerField(verbose_name='Приоритет шага')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture.object', verbose_name='Объект')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture.step', verbose_name='Шаг')),
            ],
            options={
                'ordering': ('step_priority',),
            },
        ),
    ]
