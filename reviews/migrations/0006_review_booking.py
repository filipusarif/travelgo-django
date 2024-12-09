# Generated by Django 4.2.12 on 2024-12-08 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_delete_payment'),
        ('reviews', '0005_remove_review_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='booking',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='bookings.booking'),
            preserve_default=False,
        ),
    ]
