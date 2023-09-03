# -*- coding: utf-8 -*-
import datetime
import logging
from itertools import chain
from django.conf import settings
from django.core.management import BaseCommand
from django.db import transaction

from monetary_evolution.apps.monetary.models import Monetary
from monetary_evolution.apps.repositories.api_vatcomply import RepositoryApiVatComply
from monetary_evolution.apps.services.api_vatcomply import ServiceApiVatComply

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Creates super user for local development"

    def handle(self, *args, **options):
        end = datetime.datetime.now()
        begin = end - datetime.timedelta(days=5)

        service = ServiceApiVatComply(RepositoryApiVatComply(settings.API_VAT_COMPLY))
        result = service.retrieve_variations(begin.date(), end.date())

        with transaction.atomic():
            for new_monetary in result:
                if not Monetary.objects.filter(
                    name=new_monetary.get("name"),
                    variation_date=new_monetary.get("variation_date")
                ).exists():
                    Monetary(
                        name=new_monetary.get("name"),
                        value=new_monetary.get("value"),
                        variation_date=new_monetary.get("variation_date"),
                    ).save()
