# Generated by Django 5.1.1 on 2024-09-24 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biobio', '0009_order_is_confirmed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('neck', models.CharField(blank=True, max_length=100, null=True)),
                ('chest', models.CharField(blank=True, max_length=100, null=True)),
                ('waist', models.CharField(blank=True, max_length=100, null=True)),
                ('hip', models.CharField(blank=True, max_length=100, null=True)),
                ('shoulder', models.CharField(blank=True, max_length=100, null=True)),
                ('sleeve', models.CharField(blank=True, max_length=100, null=True)),
                ('armhole', models.CharField(blank=True, max_length=100, null=True)),
                ('bicep', models.CharField(blank=True, max_length=100, null=True)),
                ('wrist', models.CharField(blank=True, max_length=100, null=True)),
                ('inseam', models.CharField(blank=True, max_length=100, null=True)),
                ('outseam', models.CharField(blank=True, max_length=100, null=True)),
                ('thigh', models.CharField(blank=True, max_length=100, null=True)),
                ('rise', models.CharField(blank=True, max_length=100, null=True)),
                ('bodylength', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
