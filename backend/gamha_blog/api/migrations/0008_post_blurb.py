# Generated by Django 5.0.2 on 2024-03-15 01:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0007_alter_post_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="blurb",
            field=models.TextField(blank=True),
        ),
    ]
