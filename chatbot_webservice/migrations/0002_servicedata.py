# Generated by Django 3.1.1 on 2020-10-11 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_webservice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DecimalField(decimal_places=4, max_digits=10)),
                ('callId', models.IntegerField()),
                ('successfulTransactions', models.IntegerField()),
                ('failedTransactions', models.IntegerField()),
                ('droppedTransactions', models.IntegerField()),
                ('avgResponseTime', models.DecimalField(decimal_places=4, max_digits=10)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='chatbot_webservice.service')),
            ],
        ),
    ]
