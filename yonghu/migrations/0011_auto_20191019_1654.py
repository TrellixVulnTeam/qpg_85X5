# Generated by Django 2.2.4 on 2019-10-19 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yonghu', '0010_auto_20191019_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=32, unique=True, verbose_name='昵称'),
        ),
    ]
