# Generated by Django 5.0.6 on 2024-06-25 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('user_id', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=150)),
                ('profile_pic_url', models.URLField()),
                ('is_verified', models.BooleanField(default=False)),
                ('is_private', models.BooleanField(null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('external_url', models.URLField(blank=True, null=True)),
                ('followers', models.IntegerField(null=True)),
                ('followees', models.IntegerField(null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('data_type', models.CharField(max_length=20)),
                ('profile_owner', models.CharField(max_length=150)),
            ],
        ),
    ]
