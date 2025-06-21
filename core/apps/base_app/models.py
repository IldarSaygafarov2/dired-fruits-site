from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата обновления", auto_now_add=True)

    class Meta:
        abstract = True
