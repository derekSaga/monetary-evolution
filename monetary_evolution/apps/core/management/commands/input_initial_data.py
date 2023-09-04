# -*- coding: utf-8 -*-
import datetime
import logging

from django.core.management import BaseCommand

from monetary_evolution.apps.monetary.service import retrieve_api_variation

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Creates super user for local development"

    def handle(self, *args, **options):
        end = datetime.datetime.now()
        begin = end - datetime.timedelta(days=5)

        retrieve_api_variation(begin.date(), end.date())
