from typing import Generic, TypeVar, Any
from abc import ABC, abstractmethod

from .Field import Field

OO = TypeVar('OO')
RO = TypeVar('RO')
P = TypeVar('P')

# *
# * Maps original object to resulting object.
# * <p>
# * OO - Original object type.
# * RO - Resulting object type.
# * P - Type of parameters object.
#
class ObjectMapper(ABC, Generic[OO, RO, P]):
    #    *
    #     * Applies translation to all specified fields.
    #     *
    #     * @param raw        Original object to translate.
    #     *                   It will be available as {@link MappingContext#originalObject}.
    #     * @param translated Resulting object to populate.
    #     *                   It will be available as {@link MappingContext#resultObject}.
    #     * @param fields     Translation map. Keys are field descriptors and
    #     *                   values specify if field is mandatory (true) or optional (false).
    #     * @param parameters Additional parameters to be passed to translator.
    #     *                   Those will be available as {@link MappingContext#parameters}.
    #     * @see FieldMapper#mapField
    #     
    @abstractmethod
    def mapAllFields(self, raw: OO, translated: RO, fields: dict[Field[OO, RO, Any, Any, P], bool], parameters: P) -> RO:
        pass
