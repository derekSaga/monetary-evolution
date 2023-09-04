# -*- coding: utf-8 -*-
from datetime import date
from datetime import timedelta

from django.conf import settings

from monetary_evolution.apps.core.service import AbstractApiService
from monetary_evolution.apps.repositories.api_vatcomply import RepositoryApiVatComply
from monetary_evolution.apps.repositories.api_vatcomply import repository_api_vat_comply


class ServiceApiVatComply(AbstractApiService):
    def __init__(self, repository: RepositoryApiVatComply):
        self.repository = repository

    def retrieve_variations(self, begin_date: date, end_date: date):
        dates = ServiceApiVatComply.dates_bwn_two_dates(begin_date, end_date)
        results = []
        for dt in dates:
            results.extend(
                self.repository.get(
                    f"{self.repository.base_url}/rates",
                    params={"date": dt.strftime(settings.DATE_FORMAT), "base": "USD"},
                )
            )
        return results

    @staticmethod
    def dates_bwn_two_dates(start_date: date, end_date: date):
        int_range = int((end_date - start_date).days)
        if int_range > 5:
            raise Exception("Período máximo de 5 dias.")
        result_return = []
        for n in range(int_range):
            result_return.append(start_date + timedelta(n))
        return result_return


service_api_vat_comply = ServiceApiVatComply(repository_api_vat_comply)
