# Generated by Django 3.2.4 on 2021-06-20 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_remove_interview_applidejob_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='applidejob_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
