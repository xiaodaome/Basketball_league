# Generated by Django 4.1 on 2023-12-15 10:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app01", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userinfo",
            name="id",
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="username",
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
