# Generated by Django 3.1.3 on 2023-01-28 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thevision', '0004_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]