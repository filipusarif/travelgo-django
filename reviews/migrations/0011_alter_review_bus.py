# Generated by Django 4.2.12 on 2024-12-08 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0003_bus_description_bus_image'),
        ('reviews', '0010_review_bus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='bus.bus'),
        ),
    ]
