# Generated by Django 5.1 on 2024-08-26 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('CLINIC', 'Clinic'), ('LAB', 'Lab')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed')], max_length=20)),
                ('finish_date', models.DateField()),
                ('delivery_method', models.CharField(choices=[('PICKUP', 'Pickup'), ('POST', 'Post'), ('EMAIL', 'Email')], max_length=10)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.user')),
            ],
        ),
    ]
