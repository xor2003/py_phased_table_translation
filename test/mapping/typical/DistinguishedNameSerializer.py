from abc import ABC
from typing import Any


class DistinguishedNameSerializer(ABC):

    def serialize(self, pairs: dict[str, Any]) -> str:
        pass
