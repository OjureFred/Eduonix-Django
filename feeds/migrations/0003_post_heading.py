# Generated by Django 4.0.3 on 2022-03-30 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0002_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='heading',
            field=models.CharField(default=11, max_length=50),
            preserve_default=False,
        ),
    ]