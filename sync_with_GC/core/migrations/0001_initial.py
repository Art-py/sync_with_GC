# Generated by Django 4.2.16 on 2024-11-24 12:01

from django.db import migrations, models
import django.db.models.deletion
import uuid6


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid6.uuid7, help_text='id записи', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='время обновления')),
                ('name', models.CharField(help_text='наименование компании', max_length=255, unique=True)),
                ('google_token', models.TextField(help_text='токен для Google API')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.UUIDField(default=uuid6.uuid7, help_text='id записи', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='время обновления')),
                ('name', models.CharField(help_text='наименование зала', max_length=255)),
                ('google_calendar_id', models.CharField(help_text='наименование google календаря', max_length=255, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='halls', to='core.company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid6.uuid7, help_text='id записи', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='время обновления')),
                ('google_id', models.CharField(help_text='идентификатор события в Google', max_length=255, unique=True)),
                ('date_start', models.DateTimeField(help_text='начало события')),
                ('date_end', models.DateTimeField(help_text='конец события')),
                ('error', models.TextField(blank=True, help_text='ошибка', null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='core.company')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='core.hall')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
