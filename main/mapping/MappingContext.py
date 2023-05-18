# pylint: disable=invalid-name
from typing import Generic, TypeVar

OO = TypeVar("OO")
RO = TypeVar("RO")
P = TypeVar("P")


class MappingContext(Generic[OO, RO, P]):
    """Contains mapping context.

    OO - Type of original object.

    RO - Type of resulting object.

    P - Type of parameters object.
    """

    def __init__(self, originalObject: OO, resultObject: RO, parameters: P):
        """:param originalObject: Original object to be translated.
        :param resultObject: Resulting object.
        :param parameters: Additional translator parameters passed from outside.
        """
        self.originalObject = originalObject
        self.resultObject = resultObject
        self.parameters = parameters
