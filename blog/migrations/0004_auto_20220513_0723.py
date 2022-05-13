# Generated by Django 4.0.4 on 2022-05-13 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_category_date_created_and_more'),
    ]

    operations = [
      migrations.RunSQL("""
        INSERT INTO blog_category (name, description, date_created, date_updated)
        VALUES ('Python', 'This is the Python category', '2020-05-13 07:23', '2020-05-13 07:23');
      """, """
        DELETE FROM blog_category 
        WHERE name = 'Python';
      """),
    ]
