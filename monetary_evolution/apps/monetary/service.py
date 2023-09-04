# -*- coding: utf-8 -*-
from datetime import date
from typing import List

from django.conf import settings
from django.contrib.postgres.aggregates import ArrayAgg
from django.db import transaction

from monetary_evolution.apps.monetary.models import Monetary
from monetary_evolution.apps.services.api_vatcomply import ServiceApiVatComply
from monetary_evolution.apps.services.api_vatcomply import service_api_vat_comply


def persist_monetary_variation(new_monetary: Monetary):
    if not Monetary.objects.filter(
            name=new_monetary.name, variation_date=new_monetary.variation_date
    ).exists():
        new_monetary.save()


def retrieve_api_variation(
        start_date: date, end_date: date, rates: List[str] = settings.RATES_DEFAULT
):
    result = service_api_vat_comply.retrieve_variations(start_date, end_date)

    with transaction.atomic():
        for new_monetary in result:
            if new_monetary.get("name") in rates:
                new_monetary = Monetary(
                    name=new_monetary.get("name"),
                    value=new_monetary.get("value"),
                    variation_date=new_monetary.get("variation_date"),
                )
                persist_monetary_variation(new_monetary)


def process_request(
        start_date: date, end_date: date
):
    dataset_dates = Monetary.objects.filter(name__in=settings.RATES_DEFAULT).filter(
        variation_date__range=(start_date, end_date)
    )

    dataset = (
        dataset_dates.values("name")
        .annotate(values=ArrayAgg("value"))
        .filter(name__in=settings.RATES_DEFAULT)
    )
    data = {
        "dates": ServiceApiVatComply.dates_bwn_two_dates(start_date, end_date),
        "data": dataset,
    }
    return {"dataset": data}
