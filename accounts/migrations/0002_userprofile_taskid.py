# Generated by Django 3.2.7 on 2021-09-30 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='taskId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
