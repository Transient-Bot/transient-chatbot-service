# Generated by Django 3.1.1 on 2020-10-11 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_webservice', '0004_auto_20201011_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause', models.CharField(max_length=200)),
                ('max_initial_loss', models.IntegerField()),
                ('max_recovery_time', models.IntegerField()),
                ('max_lor', models.IntegerField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='chatbot_webservice.service')),
            ],
        ),
    ]