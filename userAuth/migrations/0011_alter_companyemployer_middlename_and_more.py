# Generated by Django 4.1.7 on 2023-03-16 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0010_remove_company_accountpermisions_remove_company_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyemployer',
            name='middleName',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyemployer',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
