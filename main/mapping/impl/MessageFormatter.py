#*
# * Formats messages related to mapping.
# 
class MessageFormatter(GroovyObjectSupport):
    #    *
    #     * Creates a message explaining what's going on.
    #     *
    #     * @param mandatory      true if we were translating mandatory field.
    #     * @param mappingContext Translation context.
    #     * @param field          Field we were translating.
    #     * @param message        Explanation of what went wrong or what we were doing.
    #     * @return Detailed message.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull public abstract String formatMessage(@Nonnull MappingContext<?, ?, ?> mappingContext, @Nonnull Field<?, ?, ?, ?, ?> field, @Nonnull String message);
    def formatMessage(self, mappingContext, field, message):
        pass

    class WarnIfDefinedOrDataErrorAnonymousInnerClass3(WarnIfDefinedOrDataError):
        def __init__(self, defaulter, messageFormatter):
            super().__init__(defaulter, messageFormatter)

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
#ORIGINAL LINE: @Override protected String createMessage(Field field, MappingContext ctx, final MachineContext machine)
        def createMessage(self, field, ctx, machine):
            return (str((messageFormatter.invokeMethod("formatMessage", [ctx, field, "Input value is invalid: \'" + String.invokeMethod("valueOf", []) + "\'"]))))


    class WarnIfDefinedOrDataErrorAnonymousInnerClass4(WarnIfDefinedOrDataError):
        outerInstance = None

        def __init__(self, outerInstance, defaulter, messageFormatter):
            super().__init__(defaulter, messageFormatter)
            self.outerInstance = outerInstance

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
#ORIGINAL LINE: @Override protected String createMessage(Field field, MappingContext ctx, final MachineContext machine)
        def createMessage(self, field, ctx, machine):
            return (str((messageFormatter.invokeMethod("formatMessage", [ctx, field, "Input value cannot be validated: \'" + String.invokeMethod("valueOf", []) + "\'"]))))


    class WarnIfDefinedOrDataErrorAnonymousInnerClass(WarnIfDefinedOrDataError):
        outerInstance = None

        def __init__(self, outerInstance, defaulter, messageFormatter):
            super().__init__(defaulter, messageFormatter)
            self.outerInstance = outerInstance

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
#ORIGINAL LINE: @Override protected String createMessage(Field field, MappingContext ctx, final MachineContext machine)
        def createMessage(self, field, ctx, machine):
            return (str((messageFormatter.invokeMethod("formatMessage", [ctx, field, "Input value cannot be mapped: \'" + String.invokeMethod("valueOf", []) + "\'"]))))

