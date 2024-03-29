# Generated by Django 4.2.9 on 2024-04-18 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0020_remove_subcategory_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='content',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='forum/', verbose_name='Resim'),
        ),
    ]
