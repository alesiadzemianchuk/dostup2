# Generated by Django 4.1.2 on 2022-10-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dostup2app', '0005_alter_order_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='order', verbose_name='file'),
        ),
    ]
