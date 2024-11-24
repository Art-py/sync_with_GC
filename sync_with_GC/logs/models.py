from django.db import models


class LogEntry(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=50)
    message = models.TextField()
    logger = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.timestamp} - {self.level} - {self.message[:50]}..."
