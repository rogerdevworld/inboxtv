# Generated by Django 3.0.7 on 2020-10-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_userprofile_credito'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='codigo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
