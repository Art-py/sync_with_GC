from uuid6 import uuid7
from django.db import models


class BaseModel(models.Model):
    """
    Базовая модель с UUIDv7 в качестве идентификатора.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid7,
        help_text='id записи',
    )
    created_at = models.DateTimeField(auto_now_add=True, help_text='время создания')
    updated_at = models.DateTimeField(auto_now=True, help_text='время обновления')

    class Meta:
        abstract = True


class Company(BaseModel):
    name = models.CharField(max_length=255, unique=True, help_text='наименование компании')
    google_token = models.TextField(help_text='токен для Google API')

    def __str__(self):
        return self.name


class Hall(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='halls')
    name = models.CharField(max_length=255, help_text='наименование зала')
    google_calendar_id = models.CharField(max_length=255, unique=True, help_text='наименование google календаря')

    def __str__(self):
        return f"{self.name} ({self.company.name})"


class Event(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='events')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='events')
    google_id = models.CharField(max_length=255, unique=True, help_text='идентификатор события в Google')
    date_start = models.DateTimeField(help_text='начало события')
    date_end = models.DateTimeField(help_text='конец события')
    error = models.TextField(blank=True, null=True, help_text='ошибка')

    def __str__(self):
        return f"Event {self.google_id} ({self.hall.name})"
