# Generated by Django 3.1.1 on 2020-12-28 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0014_auto_20201228_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parceldelivery',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
