# Generated by Django 5.1.4 on 2025-01-15 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_epic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='id',
            options={'verbose_name': 'Айдишник', 'verbose_name_plural': 'Айдишники'},
        ),
        migrations.RemoveField(
            model_name='steam',
            name='id',
        ),
        migrations.AlterField(
            model_name='id',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Название игры'),
        ),
        migrations.AlterField(
            model_name='steam',
            name='login',
            field=models.CharField(max_length=25, primary_key=True, serialize=False, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='steam',
            name='secret_key',
            field=models.CharField(max_length=30, verbose_name='Cекретный ключ'),
        ),
    ]
