# Generated by Django 4.2.9 on 2024-04-18 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0021_alter_category_content_alter_comment_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Kategori', 'verbose_name_plural': '01-Kategoriler'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['name'], 'verbose_name': 'Alt Kategori', 'verbose_name_plural': '02-Alt Kategoriler'},
        ),
    ]