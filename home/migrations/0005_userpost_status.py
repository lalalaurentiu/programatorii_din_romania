# Generated by Django 3.2.7 on 2021-09-30 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210926_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='status',
            field=models.CharField(choices=[('Activ', 'Activ'), ('Dezactivat', 'Dezactivat'), ('In asteptare', 'In asteptare')], default='In asteptare', max_length=15),
        ),
    ]
