# Generated by Django 4.1.3 on 2022-11-29 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_chat_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 29, 8, 23, 8, 995297, tzinfo=datetime.timezone.utc)),
        ),
    ]
