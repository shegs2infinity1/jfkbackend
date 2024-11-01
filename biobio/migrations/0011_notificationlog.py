# Generated by Django 5.1.1 on 2024-10-05 13:27

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biobio', '0010_measurement'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_type', models.CharField(choices=[('email', 'Email'), ('sms', 'SMS')], max_length=10)),
                ('message', models.TextField()),
                ('recipient', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='biobio.order')),
            ],
        ),
    ]
