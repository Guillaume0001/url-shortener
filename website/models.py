from django.db import models
import uuid

def short_uuid():
    return uuid.uuid4().hex[:8]

class URL(models.Model):
    id = models.CharField(primary_key=True, default=short_uuid, max_length=8, editable=False, unique=True)
    link = models.URLField()
