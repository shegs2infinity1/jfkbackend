# Generated by Django 5.1.1 on 2024-10-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biobio', '0013_order_event_type_order_expected_date_order_material_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birthdate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]