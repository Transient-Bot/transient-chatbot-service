# Generated by Django 3.1.1 on 2020-11-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_webservice', '0013_auto_20201102_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='scenario',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=False,
        ),
    ]