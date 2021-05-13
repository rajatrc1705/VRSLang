# Generated by Django 3.1.7 on 2021-05-07 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0004_auto_20210421_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorials',
            name='description',
            field=models.CharField(default='Tutorial Description', max_length=500),
        ),
        migrations.AlterField(
            model_name='tutorials',
            name='url',
            field=models.URLField(default='https://www.youtube.com/watch?v=OmKbGOARXao', max_length=500),
        ),
    ]