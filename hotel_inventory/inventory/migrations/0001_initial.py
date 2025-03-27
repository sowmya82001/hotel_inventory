# Generated by Django 5.0.6 on 2025-03-17 06:03

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('room_number', models.CharField(max_length=10, unique=True)),
                ('room_type', models.CharField(choices=[('single', 'Single'), ('double', 'Double'), ('suite', 'Suite')], max_length=10)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.guest')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.room')),
            ],
        ),
    ]
