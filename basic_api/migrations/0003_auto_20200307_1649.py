# Generated by Django 3.0.4 on 2020-03-07 08:49

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('basic_api', '0002_auto_20200307_1635'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user_profile',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]