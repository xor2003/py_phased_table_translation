from typing import Any
from abc import ABC, abstractmethod

from ..MappingContext import MappingContext
from ..Field import Field


class MessageFormatter(ABC):
    """
    Formats messages related to mapping.
    """

    @abstractmethod
    def formatMessage(
            self,
            mappingContext: MappingContext[Any, Any, Any],
            field: Field[Any, Any, Any, Any, Any],
            message: str,
    ) -> str:
        """
        Creates a message explaining what's going on.

        :param mappingContext: Translation context.
        :param field:          Field we were translating.
        :param message:        Explanation of what went wrong or what we were doing.
        :return: Detailed message.
        """
        pass
