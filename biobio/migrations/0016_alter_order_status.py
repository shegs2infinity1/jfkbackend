# Generated by Django 5.1.1 on 2024-10-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biobio', '0015_alter_userprofile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('in_progress', 'In Progress'), ('fitting', 'fitting')], default='Pending', max_length=100),
        ),
    ]
