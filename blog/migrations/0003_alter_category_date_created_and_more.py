# Generated by Django 4.0.4 on 2022-05-13 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(null=True),
        ),
    ]