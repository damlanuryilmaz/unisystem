# Generated by Django 5.1 on 2024-08-16 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accountapp", "0003_alter_student_department_of_student"),
        ("baseapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="department_of_student",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="baseapp.department",
            ),
        ),
    ]
