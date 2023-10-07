from django.db import models
from django.utils import timezone

from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)

    @classmethod
    def api_name(self):
        return self._meta.model_name