# Generated by Django 3.2.15 on 2022-08-12 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blog_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='goal',
            field=models.TextField(),
        ),
    ]
