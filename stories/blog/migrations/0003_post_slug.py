# Generated by Django 4.1.2 on 2022-10-17 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='hello', max_length=130),
        ),
    ]
