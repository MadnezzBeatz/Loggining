# Generated by Django 5.1.4 on 2025-02-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_steam_gameclub'),
    ]

    operations = [
        migrations.AddField(
            model_name='id',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='steam',
            name='game_list',
            field=models.ManyToManyField(blank=True, related_name='games', to='accounts.id'),
        ),
    ]
