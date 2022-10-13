from django.db import models
from datetime import datetime
# Create your models here.
class ToDo_app(models.Model):
    content = models.CharField(max_length=10000)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
