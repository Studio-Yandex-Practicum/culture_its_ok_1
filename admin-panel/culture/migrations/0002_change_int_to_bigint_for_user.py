# Generated by Django 3.2 on 2023-08-28 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culture', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ('-type',), 'verbose_name': 'Шаг', 'verbose_name_plural': 'Шаги'},
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
