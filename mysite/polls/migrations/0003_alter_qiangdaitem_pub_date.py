# Generated by Django 3.2 on 2021-04-17 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_qiangdaitem_groupname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qiangdaitem',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]
