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
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class SimpleObjectMapper<OO, RO, P> extends GroovyObjectSupport implements ObjectMapper<OO, RO, P>
class SimpleObjectMapper(GroovyObjectSupport, ObjectMapper):
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override public void mapAllFields(@Nonnull OO raw, @Nonnull RO translated, @Nonnull Map<Field<OO, RO, ?, ?, P>, Boolean> fields, @Nullable P parameters)
    def mapAllFields(self, raw, translated, fields, parameters):
        assert raw is not None
        assert translated is not None
        assert fields is not None
        map = LinkedHashMap(3)
        map.put("originalObject", raw)
        map.put("resultObject", translated)
        map.put("parameters", parameters)
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final MappingContext<OO, RO, P> mappingContext = new MappingContext<OO, RO, P>(map);
        mappingContext = MappingContext(map)
        fields.invokeMethod("each", [ClosureAnonymousInnerClass(self, mappingContext)])

    class ClosureAnonymousInnerClass(Closure):


        def __init__(self, outerInstance, mappingContext):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self._mappingContext = mappingContext

        def doCall(self, field, mandatory):
            return (getMandatoryFieldMapper() if mandatory else getOptionalFieldMapper()).invokeMethod("mapField", [field, self._mappingContext])


    def getOptionalFieldMapper(self):
        return optionalFieldMapper

    def setOptionalFieldMapper(self, optionalFieldMapper):
        self.optionalFieldMapper = optionalFieldMapper

    def getMandatoryFieldMapper(self):
        return mandatoryFieldMapper

    def setMandatoryFieldMapper(self, mandatoryFieldMapper):
        self.mandatoryFieldMapper = mandatoryFieldMapper

    #    *
    #     * Mapper for optional fields.
    #     * <p>
    #     * By default, this is {@link OptionalFieldMapper}.
    #     
    #    *
    #     * Mapper for mandatory fields.
    #     * <p>
    #     * By default, this is {@link MandatoryFieldMapper}.
    #     
