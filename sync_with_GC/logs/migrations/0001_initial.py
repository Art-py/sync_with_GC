# Generated by Django 4.2.16 on 2024-11-24 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('level', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('logger', models.CharField(max_length=255)),
            ],
        ),
    ]
