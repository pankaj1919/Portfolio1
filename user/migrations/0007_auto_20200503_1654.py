# Generated by Django 3.0.5 on 2020-05-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='media/profile/man-logo.png', null=True, upload_to='profile/', verbose_name='Upload Client Image'),
        ),
    ]