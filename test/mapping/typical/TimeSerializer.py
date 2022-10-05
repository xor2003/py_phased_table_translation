from abc import ABC


class TimeSerializer(ABC):
    def serialize(self, time) -> str:
        pass

