# Generated by Django 5.0.4 on 2024-04-07 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0010_alter_option_option_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_number',
        ),
    ]
