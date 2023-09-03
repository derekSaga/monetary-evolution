# -*- coding: utf-8 -*-
from abc import ABC
from abc import abstractmethod


class AbstractApiRepository(ABC):
    def __init__(self, base_url):
        self.base_url = base_url

    @abstractmethod
    def get(self, endpoint):
        pass
