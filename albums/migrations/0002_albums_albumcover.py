# Generated by Django 3.0.7 on 2020-06-29 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='albums',
            name='albumcover',
            field=models.ImageField(default='blank.jpg', upload_to='images/'),
        ),
    ]