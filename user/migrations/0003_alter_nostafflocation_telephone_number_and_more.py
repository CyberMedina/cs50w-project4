# Generated by Django 4.2.7 on 2023-12-02 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_nostafflocation_telephone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nostafflocation',
            name='telephone_Number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='stafflocation',
            name='telephone_Number',
            field=models.CharField(max_length=15),
        ),
    ]
