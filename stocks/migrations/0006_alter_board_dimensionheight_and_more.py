# Generated by Django 4.1.7 on 2023-03-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_alter_board_dimensionheight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='dimensionHeight',
            field=models.IntegerField(default=2800),
        ),
        migrations.AlterField(
            model_name='board',
            name='dimensionLength',
            field=models.IntegerField(default=2070),
        ),
        migrations.AlterField(
            model_name='board',
            name='dimensionWidth',
            field=models.IntegerField(default=18),
        ),
    ]
