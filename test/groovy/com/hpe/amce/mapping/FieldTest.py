class FieldTest(Specification):
    def construct_via_fluent_API_with_closure_parameters_and_delegate_help_from_IDE(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        field = (Field()).invokeMethod("withId", ["notificationIdentifier"]).invokeMethod("withGetter", [ClosureAnonymousInnerClass(self)]).invokeMethod("withValidator", {Closure(self, self){public Boolean doCall(Object it){return it != parameters.parameter

    class ClosureAnonymousInnerClass(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance

        def doCall(self, it):
            return it.identifier

        def doCall(self):
            return self.doCall(None)


    def doCall(self):
        return doCall(None)

}
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
).invokeMethod("withDefaulter", new Object[]{new Closure(self, self)
    def doCall(self, it):
        return 777

    def doCall(self):
        return doCall(None)

}
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
).invokeMethod("withTranslator", new Object[]{new Closure(self, self)
    def doCall(self, it):
        return Long.invokeMethod("parseLong", [it])

    def doCall(self):
        return doCall(None)

}
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
).invokeMethod("withSetter", new Object[]{new Closure(self, self)
    def doCall(self, it):
        return resultObject.notificationIdentifier = it

    def doCall(self):
        return doCall(None)

}
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
);
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#then:
field.id == "notificationIdentifier"
field.getter
field.validator
field.defaulter
field.translator
return field.setter
}

private static class Original extends GroovyObjectSupport
    public String getIdentifier()
        return identifier

    public void setIdentifier(String identifier)
        self.identifier = identifier

    private String identifier

private static class Result extends GroovyObjectSupport
    public Long getNotificationIdentifier()
        return notificationIdentifier

    public void setNotificationIdentifier(Long notificationIdentifier)
        self.notificationIdentifier = notificationIdentifier

    private Long notificationIdentifier

private static class Params extends GroovyObjectSupport
    public String getParameter()
        return parameter

    public void setParameter(String parameter)
        self.parameter = parameter

    private String parameter

private static <T> T com.hpe.amce.mapping._setGroovyRef(groovy.lang.Reference<T> ref, T newValue)
    ref.set(newValue)
    return newValue
}
