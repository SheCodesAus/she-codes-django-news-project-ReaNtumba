# Generated by Django 4.1.3 on 2022-12-10 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newsstory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image',
            field=models.TextField(max_length=250, null=True),
        ),
    ]
