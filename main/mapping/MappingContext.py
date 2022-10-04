#*
# * Contains mapping context.
# * <p>
# * OO - Type of original object.
# * RO - Type of resulting object.
# * P - Type of parameters object.
# 

from typing import Generic, TypeVar, Any

OO = TypeVar('OO')
RO = TypeVar('RO')
P = TypeVar('P')

class MappingContext(Generic[OO, RO, P]):

    def __init__(self, originalObject: OO = None,
        resultObject: RO = None,
        parameters: P = None):
        #     * Original object to be translated.
        #
        #     * Resulting object.
        #
        #     * Additional translator parameters passed from outside.
        #
        self.originalObject: OO = originalObject
        self.resultObject: RO = resultObject
        self.parameters: P = parameters

