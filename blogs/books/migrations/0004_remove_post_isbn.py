# Generated by Django 2.2.1 on 2019-09-05 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20190531_0633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='isbn',
        ),
    ]
