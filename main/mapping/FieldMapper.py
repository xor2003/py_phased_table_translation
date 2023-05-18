# pylint: disable=invalid-name
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Any

from .Field import Field
from .MappingContext import MappingContext

OO = TypeVar("OO")
RO = TypeVar("RO")
P = TypeVar("P")


class FieldMapper(ABC, Generic[OO, RO, P]):
    """Maps single field from original object to result object.

    OO - Original object type.

    RO - Resulting object type.

    P - Type of parameters object.
    """

    @abstractmethod
    def mapField(
            self,
            field: Field[OO, RO, Any, Any, P],
            mappingContext: MappingContext[OO, RO, P],
    ):
        """> Applies processing to specified field.

        :param field: Field descriptor telling how to extract, map and inject field value
                      from original to resulting object.
        :param mappingContext: Translation context containing original and result objects.
        """
        pass
