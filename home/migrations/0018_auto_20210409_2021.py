# Generated by Django 3.1.6 on 2021-04-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_delete_reserve'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartypes',
            name='slug',
        ),
        migrations.AddField(
            model_name='cartypes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cat_imgs/'),
        ),
    ]
