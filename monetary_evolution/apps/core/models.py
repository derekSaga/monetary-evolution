# -*- coding: utf-8 -*-
from uuid import uuid4

from django.db import models


class StandardModelMixin(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, verbose_name="Id"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Data de criação"
    )
    updated_at = models.DateTimeField(
        auto_now=True, editable=False, verbose_name="Data da última atualização"
    )

    class Meta:
        abstract = True
