# Generated by Django 4.2.6 on 2023-11-01 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_remove_player_assists_remove_player_goals_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboardstats',
            name='date',
        ),
    ]
