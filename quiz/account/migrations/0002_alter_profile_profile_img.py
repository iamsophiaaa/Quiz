# Generated by Django 5.0.4 on 2024-04-09 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to='profile_image'),
        ),
    ]
