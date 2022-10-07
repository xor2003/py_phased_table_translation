from abc import ABC
from typing import Any, Dict


class DistinguishedNameSerializer(ABC):

    def serialize(self, pairs: Dict[str, Any]) -> str:
        pass
