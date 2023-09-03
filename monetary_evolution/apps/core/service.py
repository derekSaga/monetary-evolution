# -*- coding: utf-8 -*-
import abc
from abc import ABC

from monetary_evolution.apps.core.repository import AbstractApiRepository


class AbstractApiService(ABC):
    @abc.abstractmethod
    def __init__(self, repository: AbstractApiRepository):
        self.repository = repository
