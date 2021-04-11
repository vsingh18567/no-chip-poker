# Generated by Django 3.2 on 2021-04-10 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pokerapi", "0004_alter_game_time_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="current_player",
            field=models.ForeignKey(
                blank=True,
                default=None,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="games_current_player",
                to="pokerapi.player",
            ),
        ),
    ]
