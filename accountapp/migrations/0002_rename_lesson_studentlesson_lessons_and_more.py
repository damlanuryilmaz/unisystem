# Generated by Django 5.1 on 2024-08-15 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accountapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="studentlesson",
            old_name="lesson",
            new_name="lessons",
        ),
        migrations.RenameField(
            model_name="studentlesson",
            old_name="student",
            new_name="students",
        ),
    ]
