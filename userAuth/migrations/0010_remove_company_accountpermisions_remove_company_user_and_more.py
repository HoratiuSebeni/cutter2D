# Generated by Django 4.1.7 on 2023-03-16 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0009_company_rename_childuser_companyemployer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='accountPermisions',
        ),
        migrations.RemoveField(
            model_name='company',
            name='user',
        ),
        migrations.AlterField(
            model_name='company',
            name='company',
            field=models.TextField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='companyemployer',
            name='accountPermisions',
            field=models.CharField(default='admin', max_length=20),
        ),
    ]
