# Generated by Django 5.0.4 on 2024-04-07 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_remove_question_question_number_question_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_number',
            field=models.IntegerField(default=0),
        ),
    ]
