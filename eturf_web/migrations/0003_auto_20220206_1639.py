# Generated by Django 3.2.7 on 2022-02-06 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eturf_web', '0002_alter_userdb_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdb',
            name='ground',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bookdb',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]