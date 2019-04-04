# Generated by Django 2.1.5 on 2019-03-27 08:50

import datetime
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mucluc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mucluc', models.CharField(max_length=200, verbose_name='Mục lục')),
                ('noidung', models.TextField(verbose_name='Nội dung')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Ngày:')),
            ],
            managers=[
                ('mucluc1', django.db.models.manager.Manager()),
            ],
        ),
    ]
