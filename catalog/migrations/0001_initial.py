# Generated by Django 4.1.5 on 2023-01-29 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=250, verbose_name='Slug')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Изображение')),
                ('date_create', models.DateTimeField(verbose_name='Дата создания')),
                ('publication', models.CharField(choices=[('active', 'Опубликован'), ('inactive', 'Не опубликован')], default='active', max_length=250, verbose_name='Признак публикации')),
                ('views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('title', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('title', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Изображение')),
                ('category', models.CharField(max_length=250, verbose_name='Категория')),
                ('price', models.FloatField(verbose_name='Цена за покупку')),
                ('date_create', models.DateTimeField(verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(verbose_name='Дата последнего изменения')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField(default=1, verbose_name='Номер версии')),
                ('name', models.CharField(max_length=250, verbose_name='Название версии')),
                ('status', models.CharField(choices=[('active', 'активная'), ('inactive', 'неактивная')], default='inactive', max_length=50, verbose_name='Признак версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
        ),
    ]
