from abc import ABC

from Exchange import Exchange


class ExchangeFormatter(ABC):
    def format(self, exchange: Exchange) -> str:
        pass
