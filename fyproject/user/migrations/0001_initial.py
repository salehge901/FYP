# Generated by Django 3.2.4 on 2021-06-20 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0010_interview_applidejob_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewQuestions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('question_id', models.IntegerField()),
                ('job_id', models.IntegerField()),
                ('job_title', models.CharField(max_length=200)),
                ('question', models.CharField(max_length=300)),
                ('question_answer', models.CharField(max_length=800)),
                ('candidate_answer', models.CharField(max_length=800)),
                ('Interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.interview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
