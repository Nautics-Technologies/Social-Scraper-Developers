# Generated by Django 5.0.6 on 2024-06-25 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='scrapeddata',
            unique_together={('username', 'data_type', 'profile_owner')},
        ),
    ]
