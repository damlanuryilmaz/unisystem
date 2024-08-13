# Generated by Django 5.0.7 on 2024-08-11 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapp', '0020_rename_student_grade_grade_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='grade_type',
        ),
        migrations.AddField(
            model_name='grade',
            name='grade_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.CharField(choices=[(4.0, 'AA'), (3.7, 'BA'), (3.3, 'BB'), (3.0, 'CB'), (2.7, 'CC'), (2.3, 'DC'), (2.0, 'DD'), (1.7, 'FD'), (0.0, 'FF')], max_length=2),
        ),
    ]
