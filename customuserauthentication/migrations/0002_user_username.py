# Generated by Django 4.2 on 2023-04-16 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuserauthentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
