# Generated by Django 3.0.5 on 2020-05-06 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Category Name')),
            ],
            options={
                'verbose_name_plural': 'Portfolio Category',
            },
        ),
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='portfolio/', verbose_name='Upload Image')),
                ('link', models.CharField(blank=True, max_length=100, null=True, verbose_name='Project Link')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Project Name')),
                ('icon', models.CharField(blank=True, max_length=100, null=True, verbose_name='Write Icon Name')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolios.Category')),
            ],
            options={
                'verbose_name_plural': 'Portfolio',
            },
        ),
    ]
