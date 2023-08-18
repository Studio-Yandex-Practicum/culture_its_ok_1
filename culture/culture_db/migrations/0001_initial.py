# Generated by Django 3.2 on 2023-08-18 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('author', models.CharField(blank=True, max_length=255, null=True, verbose_name='Автор')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('how_to_get', models.TextField(blank=True, null=True, verbose_name='Как добраться')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название маршрута')),
                ('photo', models.ImageField(upload_to='photos', verbose_name='Фото маршрута')),
                ('description', models.TextField(verbose_name='Описание маршрута')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес маршрута')),
                ('welcome_message', models.TextField(blank=True, null=True, verbose_name='Приветственное сообщение')),
                ('goodbye_message', models.TextField(blank=True, null=True, verbose_name='Прощальное сообщение')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршруты',
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('text', 'Текст'), ('photo', 'Фото'), ('reflection', 'Рефлексия'), ('continue_button', 'Кнопка продолжить')], max_length=20, verbose_name='Тип шага')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Контент шага')),
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('age', models.IntegerField(verbose_name='Возраст')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='RouteObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_priority', models.IntegerField(verbose_name='Приоритет')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture_db.object', verbose_name='Объект')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture_db.route', verbose_name='Маршрут')),
            ],
            options={
                'verbose_name': 'Путь к объекту',
                'verbose_name_plural': 'Пути к объектам',
                'ordering': ('-object_priority',),
            },
        ),
        migrations.CreateModel(
            name='Reflection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('text', 'Текст'), ('voice', 'Голос')], max_length=10, verbose_name='Тип')),
                ('content', models.TextField(verbose_name='Контент')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture_db.object', verbose_name='Объект')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture_db.route', verbose_name='Путь')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture_db.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Рефлексия',
                'verbose_name_plural': 'Рефлексия',
            },
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField(auto_now_add=True, verbose_name='Время начала')),
                ('finished_at', models.DateTimeField(blank=True, null=True, verbose_name='Время конца')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture_db.object', verbose_name='Объект')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture_db.route', verbose_name='Путь')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture_db.user', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Прогресс пользователя',
                'verbose_name_plural': 'Прогресс пользователей',
                'ordering': ('-started_at',),
            },
        ),
        migrations.CreateModel(
            name='ObjectStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_priority', models.IntegerField(verbose_name='Приоритет шага')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture_db.object', verbose_name='Объект')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture_db.step', verbose_name='Шаг')),
            ],
            options={
                'verbose_name': 'Шаг к объекту',
                'verbose_name_plural': 'Шаги к объектам',
                'ordering': ('-step_priority',),
            },
        ),
    ]
