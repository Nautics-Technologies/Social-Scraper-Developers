# Generated by Django 5.0.6 on 2024-06-27 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_instagramprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramprofile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='instagramprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='instagramprofile',
            name='external_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='instagramprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='instagramprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='instagramprofile',
            name='profile_pic',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='instagramprofile',
            name='user_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='instagramprofile',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
