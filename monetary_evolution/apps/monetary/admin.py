# -*- coding: utf-8 -*-
# Define the admin class
from django.contrib import admin

from monetary_evolution.apps.monetary.models import Monetary


class MonetaryAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(Monetary, MonetaryAdmin)
