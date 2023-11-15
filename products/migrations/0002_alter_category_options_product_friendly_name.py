# Generated by Django 4.2.7 on 2023-11-15 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
