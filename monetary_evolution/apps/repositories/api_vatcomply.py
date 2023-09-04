# -*- coding: utf-8 -*-
from typing import Dict
from typing import List

import requests
from django.conf import settings

from monetary_evolution.apps.core.repository import AbstractApiRepository


class RepositoryApiVatComply(AbstractApiRepository):
    RATES = settings.RATES_DEFAULT

    def get(
        self,
        endpoint: str,
        headers: Dict = None,
        params: Dict = None,
    ) -> List[Dict]:
        response = requests.get(endpoint, headers=headers or {}, params=params or {})
        response_json = response.json()
        rates_response = response_json.get("rates")
        result = [
            {
                "name": key,
                "value": value,
                "variation_date": response_json.get("date"),
            }
            for key, value in rates_response.items()
        ]
        return result


repository_api_vat_comply = RepositoryApiVatComply(settings.API_VAT_COMPLY)
