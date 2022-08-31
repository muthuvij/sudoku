# Generated by Django 3.2.15 on 2022-08-12 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', models.TextField(blank=True, null=True)),
                ('age', models.DecimalField(decimal_places=1, max_digits=2)),
                ('goal', models.TextField()),
            ],
        ),
    ]