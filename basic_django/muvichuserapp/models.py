from django.conf import settings
from django.db import models
from django.utils import timezone


class Movie(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    class Priority(models.TextChoices):
        HIGH = "1"
        MEDIUM = "2"
        LOW = "3"

    priority = models.CharField(
        max_length=1,
        choices=Priority.choices,
        default=Priority.HIGH,
    )


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title