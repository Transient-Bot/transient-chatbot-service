# Generated by Django 3.1.1 on 2020-11-01 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_webservice', '0012_dependency_system'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicedata',
            name='droppedTransactions',
        ),
        migrations.RemoveField(
            model_name='servicedata',
            name='failedTransactions',
        ),
        migrations.RemoveField(
            model_name='servicedata',
            name='successfulTransactions',
        ),
    ]