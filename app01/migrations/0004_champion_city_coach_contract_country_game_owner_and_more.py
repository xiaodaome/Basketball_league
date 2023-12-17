# Generated by Django 4.1 on 2023-12-15 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app01", "0003_alter_userinfo_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="Champion",
            fields=[
                ("year", models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "champion",
            },
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "name",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("state", models.CharField(max_length=30)),
            ],
            options={
                "db_table": "city",
            },
        ),
        migrations.CreateModel(
            name="Coach",
            fields=[
                (
                    "name",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("age", models.IntegerField()),
                ("CoachingExperience", models.IntegerField()),
            ],
            options={
                "db_table": "coach",
            },
        ),
        migrations.CreateModel(
            name="Contract",
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
                ("salary", models.IntegerField()),
                ("StartDate", models.DateField()),
                ("EndDate", models.DateField()),
            ],
            options={
                "db_table": "contract",
            },
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "name",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("continent", models.CharField(max_length=30)),
                ("rank", models.IntegerField()),
                ("national_league", models.CharField(max_length=30)),
            ],
            options={
                "db_table": "country",
            },
        ),
        migrations.CreateModel(
            name="Game",
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
                ("home_score", models.IntegerField()),
                ("away_score", models.IntegerField()),
                ("date", models.DateField()),
            ],
            options={
                "db_table": "game",
            },
        ),
        migrations.CreateModel(
            name="Owner",
            fields=[
                (
                    "name",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("corporation", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
            ],
            options={
                "db_table": "owner",
            },
        ),
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "name",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("age", models.IntegerField()),
                ("height", models.IntegerField()),
                ("pos", models.IntegerField()),
                ("country", models.CharField(max_length=30)),
            ],
            options={
                "db_table": "player",
            },
        ),
        migrations.CreateModel(
            name="Season",
            fields=[
                ("year", models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "season",
            },
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "name",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("arena", models.CharField(max_length=100)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app01.city"
                    ),
                ),
            ],
            options={
                "db_table": "team",
            },
        ),
        migrations.DeleteModel(
            name="USERINFO",
        ),
        migrations.AddField(
            model_name="season",
            name="champion",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app01.team"
            ),
        ),
        migrations.AddField(
            model_name="season",
            name="mvp",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mvp",
                to="app01.player",
            ),
        ),
        migrations.AddField(
            model_name="season",
            name="scoring_title",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scoring_title",
                to="app01.player",
            ),
        ),
        migrations.AddField(
            model_name="player",
            name="team",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="app01.team"
            ),
        ),
        migrations.AddField(
            model_name="owner",
            name="team",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="app01.team"
            ),
        ),
        migrations.AddField(
            model_name="game",
            name="away",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="away_team",
                to="app01.team",
            ),
        ),
        migrations.AddField(
            model_name="game",
            name="home",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="home_team",
                to="app01.team",
            ),
        ),
        migrations.AddField(
            model_name="contract",
            name="player",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app01.player"
            ),
        ),
        migrations.AddField(
            model_name="contract",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app01.team"
            ),
        ),
        migrations.AddField(
            model_name="coach",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app01.team"
            ),
        ),
        migrations.AddField(
            model_name="champion",
            name="fmvp",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app01.player"
            ),
        ),
        migrations.AddField(
            model_name="champion",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app01.team"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="game",
            unique_together={("home", "date")},
        ),
        migrations.CreateModel(
            name="Draft",
            fields=[
                ("year", models.IntegerField()),
                ("pick", models.IntegerField()),
                (
                    "player",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="app01.player",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app01.team"
                    ),
                ),
            ],
            options={
                "db_table": "draft",
            },
        ),
        migrations.AlterUniqueTogether(
            name="contract",
            unique_together={("player", "team", "StartDate")},
        ),
    ]