# Generated by Django 3.0.7 on 2020-10-12 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Anime', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anime',
            options={'ordering': ['lugar'], 'verbose_name': 'Anime', 'verbose_name_plural': 'Animes'},
        ),
    ]
