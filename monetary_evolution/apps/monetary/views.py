# -*- coding: utf-8 -*-
import datetime

from django.conf import settings
from django.shortcuts import render

from monetary_evolution.apps.monetary.service import process_request
from monetary_evolution.apps.monetary.service import retrieve_api_variation


# Create your views here.
def show_graph(request):
    end = datetime.datetime.utcnow()
    begin = end - datetime.timedelta(days=5)
    rates = settings.RATES_DEFAULT
    if request.method == "POST":
        rates[0] = request.POST.get("currency_one")
        rates[1] = request.POST.get("currency_second")
        rates[2] = request.POST.get("currency_third")
        retrieve_api_variation(begin, end, rates)
    data = process_request(begin, end)
    return render(request, "charts/index.html", data)
