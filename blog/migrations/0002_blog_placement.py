# Generated by Django 3.2.15 on 2022-08-12 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='placement',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
