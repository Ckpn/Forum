# Generated by Django 4.2.9 on 2024-03-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_alter_comment_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Başlık'),
        ),
    ]
