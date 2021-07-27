# Generated by Django 3.2.5 on 2021-07-27 04:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='sent_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_that_sent_notification', to=settings.AUTH_USER_MODEL),
        ),
    ]
