# Generated by Django 5.1.1 on 2024-10-19 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_profile_delete_userprofile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("recipe_name", models.CharField(max_length=100)),
                ("recipe_description", models.TextField()),
                (
                    "recipe_image",
                    models.ImageField(blank=True, null=True, upload_to="recipe"),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
