# Generated by Django 5.1.1 on 2024-10-11 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biobio', '0014_userprofile_birthdate_userprofile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
