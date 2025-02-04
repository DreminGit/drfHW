import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название курса')),
                ('image', models.ImageField(blank=True, null=True, upload_to='school/course_images', verbose_name='Превью картинка курса')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание курса')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название урока')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание урока')),
                ('image', models.ImageField(blank=True, null=True, upload_to='school/lesson_images', verbose_name='Превью картинка урока')),
                ('video_link', models.URLField(blank=True, max_length=250, null=True, verbose_name='Ссылка на видео')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='lms.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
    ]