# Generated by Django 3.1.6 on 2021-02-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lopsinhvien', '0003_auto_20210206_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='tieusu',
        ),
        migrations.AddField(
            model_name='student',
            name='detail_per',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
