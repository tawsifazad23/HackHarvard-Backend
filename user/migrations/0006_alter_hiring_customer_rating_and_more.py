# Generated by Django 4.2.13 on 2024-08-10 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_alter_user_profile_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hiring",
            name="customer_rating",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="hiring",
            name="service_provider_rating",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
