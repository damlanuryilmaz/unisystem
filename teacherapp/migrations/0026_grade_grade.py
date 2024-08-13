# Generated by Django 5.0.7 on 2024-08-12 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapp', '0025_remove_grade_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='grade',
            field=models.FloatField(choices=[(4.0, 'AA'), (3.7, 'BA'), (3.3, 'BB'), (3.0, 'CB'), (2.7, 'CC'), (2.3, 'DC'), (2.0, 'DD'), (1.7, 'FD'), (0.0, 'FF')], default=0.0),
        ),
    ]
