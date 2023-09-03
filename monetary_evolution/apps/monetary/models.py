# -*- coding: utf-8 -*-

from django.db import models

from monetary_evolution.apps.core.models import StandardModelMixin


class Monetary(StandardModelMixin):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "variation_date"],
                name="unique_name_variation_date",
            ),
        ]

    name = models.CharField(
        max_length=5,
    )

    value = models.DecimalField(decimal_places=5, max_digits=10)
    variation_date = models.DateTimeField(
        verbose_name="Data da variação",
        null=False,
    )

    def get_variation_date(self):
        return self.variation_date.strftime("%Y-%m-%d")

    def __str__(self):
        return f"{self.name} - {self.variation_date.date()}"
