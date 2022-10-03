#*
# * Message formatter that puts all information on single line.
# * <p>
# * Information that is added:
# * <ul>
# *     <li>type of field: optional/mandatory</li>
# *     <li>input object</li>
# *     <li>mapping parameters</li>
# *     <li>field identifier</li>
# *     <li>provided message</li>
# * </ul>
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class SingleLineMesasgeFormatter extends GroovyObjectSupport implements MessageFormatter
class SingleLineMesasgeFormatter(GroovyObjectSupport, MessageFormatter):

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self._mandatory = False

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override @Nonnull public String formatMessage(@Nonnull final MappingContext<?, ?, ?> mappingContext, @Nonnull final Field<?, ?, ?, ?, ?> field, @Nonnull String message)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
    def formatMessage(self, mappingContext, field, message):
        optionality = "mandatory" if self._mandatory else "optional"
        return (str((String.invokeMethod("valueOf", [message]) + " for " + optionality + " field " + String.invokeMethod("valueOf", [field.id]) + "." + " On: ~~~>" + String.invokeMethod("valueOf", [mappingContext.originalObject]) + "<~~~" + " Parameters: " + String.invokeMethod("valueOf", [mappingContext.parameters]) + ".")))

    def getMandatory(self):
        return self._mandatory

    def isMandatory(self):
        return self._mandatory

    def setMandatory(self, mandatory):
        self._mandatory = mandatory

    #    *
    #     * Indicates if the field is mandatory.
    #     
