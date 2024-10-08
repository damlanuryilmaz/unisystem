# Generated by Django 5.1 on 2024-08-26 07:59

from django.db import migrations
from django.utils.text import slugify


def populate_slugs(apps, schema_editor):
    Lesson = apps.get_model('baseapp', 'Lesson')
    for lesson in Lesson.objects.all():
        if not lesson.slug:
            lesson.slug = slugify(lesson.title)
            lesson.save()


class Migration(migrations.Migration):

    dependencies = [
        ("baseapp", "0015_alter_lesson_slug"),
    ]

    operations = [
        migrations.RunPython(populate_slugs),
    ]
