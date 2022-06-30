# Generated by Django 4.0.1 on 2022-06-26 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_mgt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(max_length=100, null=b'I01\n'),
            preserve_default=b'I01\n',
        ),
        migrations.AddField(
            model_name='post',
            name='state',
            field=models.CharField(max_length=100, null=b'I01\n'),
            preserve_default=b'I01\n',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='food_pics'),
        ),
    ]
