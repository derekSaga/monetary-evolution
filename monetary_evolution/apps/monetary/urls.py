# -*- coding: utf-8 -*-

from django.urls import path

from monetary_evolution.apps.monetary.views import show_graph

urlpatterns = [path("", show_graph, name="monetary")]
