#*
# * Simple object mapper that applies fields mappers
# * one-by-one in the same thread in the specified order.
# * <p>
# * Mandatory fields are mapped using {@link SimpleObjectMapper#mandatoryFieldMapper}
# * while optional fields are mapped using {@link SimpleObjectMapper#optionalFieldMapper}.
# * <p>
# * OO - Original object type.
# * RO - Resulting object type.
# * P - Type of parameters object.
#

from typing import Generic, TypeVar, Any

from ..Field import Field
from ..FieldMapper import FieldMapper
from ..MappingContext import MappingContext
from ..ObjectMapper import ObjectMapper
from .OptionalFieldMapper import OptionalFieldMapper
from .MandatoryFieldMapper import MandatoryFieldMapper

OO = TypeVar('OO')
RO = TypeVar('RO')
P = TypeVar('P')


class SimpleObjectMapper(Generic[OO, RO, P], ObjectMapper[OO, RO, P]):

    def __init__(self):
        self.optionalFieldMapper: FieldMapper[OO, RO, P] = OptionalFieldMapper[OO, RO, P]()
        self.mandatoryFieldMapper: FieldMapper[OO, RO, P] = MandatoryFieldMapper[OO, RO, P]()

    def mapAllFields(self, raw: OO, translated: RO, fields: dict[Field[OO, RO, Any, Any, P], bool], parameters: P) -> RO:
        assert raw is not None
        assert translated is not None
        assert fields
        mappingContext = MappingContext[OO, RO, P](originalObject=raw, resultObject=translated, parameters=parameters)
        for field, mandatory in fields.items():
            (self.mandatoryFieldMapper if mandatory else self.optionalFieldMapper).mapField(field, mappingContext)
        return mappingContext.resultObject

