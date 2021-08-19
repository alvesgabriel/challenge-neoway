from django.db import models


class File(models.Model):
    filename = models.FileField()
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
