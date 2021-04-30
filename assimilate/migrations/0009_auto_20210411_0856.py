# Generated by Django 2.2.19 on 2021-04-11 03:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assimilate', '0008_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whole_user', to=settings.AUTH_USER_MODEL),
        ),
    ]