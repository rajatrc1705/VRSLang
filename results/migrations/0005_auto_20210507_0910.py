# Generated by Django 3.1.7 on 2021-05-07 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0004_alter_result_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]