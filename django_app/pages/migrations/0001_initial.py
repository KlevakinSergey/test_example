# Generated by Django 3.1.5 on 2021-01-17 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Телефон')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='site_images')),
            ],
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='site_images')),
                ('title_main_image_1', models.CharField(blank=True, max_length=255, null=True)),
                ('title_main_image_2', models.CharField(blank=True, max_length=255, null=True)),
                ('title_about_project', models.TextField(blank=True, null=True)),
                ('text_about_project', models.TextField(blank=True, null=True)),
                ('count_flats', models.CharField(blank=True, max_length=255, null=True)),
                ('about_project_image_1', models.ImageField(blank=True, null=True, upload_to='site_images')),
                ('about_project_image_2', models.ImageField(blank=True, null=True, upload_to='site_images')),
                ('about_project_image_3', models.ImageField(blank=True, null=True, upload_to='site_images')),
                ('architecture_title', models.TextField(blank=True, null=True)),
                ('architecture_text', models.TextField(blank=True, null=True)),
                ('developer_text', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Blog 1',
                'verbose_name_plural': 'Blog 1',
            },
        ),
    ]