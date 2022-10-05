//====================================================================================================
//The Free Edition of Java to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================

class MapperTest(Specification):
    def setup(self):
        listAppender.invokeMethod("clear", [])

    @staticmethod
    def cfg(optional, getter, validator, defaulter, translator, setter, desiredFieldResult, desiredLogResult):
        pass

    def isConfigError(self, cfg):
        return (cfg.getGetter() == com.hpe.amce.mapping.MapperTest.Get.Undef and cfg.getDefaulter() == com.hpe.amce.mapping.MapperTest.Def.Undef) or (cfg.getSetter() == com.hpe.amce.mapping.MapperTest.Set.Undef and (cfg.getValidator() == com.hpe.amce.mapping.MapperTest.Val.Undef or cfg.getDefaulter() != com.hpe.amce.mapping.MapperTest.Def.Undef or cfg.getTranslator() != com.hpe.amce.mapping.MapperTest.Tr.Undef))

    def shouldDefaulterBeCalled(self, cfg):
        if self.isConfigError(cfg):
            return False

        return cfg.getGetter() in_ list(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Get.Undef, com.hpe.amce.mapping.MapperTest.Get.Ex, com.hpe.amce.mapping.MapperTest.Get.Null)) or cfg.getValidator() in_ list(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Val.Ex, com.hpe.amce.mapping.MapperTest.Val.Bad)) or cfg.getTranslator() == com.hpe.amce.mapping.MapperTest.Tr.Ex

    def shouldTranslatorBeCalled(self, cfg):
        if self.isConfigError(cfg):
            return False

        return cfg.getGetter() == com.hpe.amce.mapping.MapperTest.Get.Some and cfg.getValidator() in_ list(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Val.Undef, com.hpe.amce.mapping.MapperTest.Val.Ok))

    def shouldWarn(self, cfg):
        if self.isConfigError(cfg):
            return False

        if cfg.getOptional() == com.hpe.amce.mapping.MapperTest.Opt.M and cfg.getDefaulter() != com.hpe.amce.mapping.MapperTest.Def.Undef.asBoolean():
            return cfg.getGetter() in_ list(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Get.Ex, com.hpe.amce.mapping.MapperTest.Get.Null)) or (cfg.getGetter() == com.hpe.amce.mapping.MapperTest.Get.Some and (cfg.getValidator() in_ list(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Val.Ex, com.hpe.amce.mapping.MapperTest.Val.Bad)) or cfg.getTranslator() == com.hpe.amce.mapping.MapperTest.Tr.Ex))
        elif cfg.getOptional() == com.hpe.amce.mapping.MapperTest.Opt.O.asBoolean():
            return cfg.getGetter() in_ list(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Get.Ex)) or (cfg.getGetter() == com.hpe.amce.mapping.MapperTest.Get.Some and (cfg.getValidator() in_ list(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Val.Ex, com.hpe.amce.mapping.MapperTest.Val.Bad)) or cfg.getTranslator() == com.hpe.amce.mapping.MapperTest.Tr.Ex))
        else:
            return False


    def shouldSetterBeCalled(self, cfg):
        if self.isConfigError(cfg):
            return False

        return (cfg.getGetter() == com.hpe.amce.mapping.MapperTest.Get.Some and cfg.getValidator() in_ list(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Val.Undef, com.hpe.amce.mapping.MapperTest.Val.Ok)) and (cfg.getTranslator() in_ list(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Tr.Some, com.hpe.amce.mapping.MapperTest.Tr.Undef)) or (cfg.getOptional() == com.hpe.amce.mapping.MapperTest.Opt.O and cfg.getTranslator() == com.hpe.amce.mapping.MapperTest.Tr.Null))) or cfg.getDefaulter() == com.hpe.amce.mapping.MapperTest.Def.Some

    def getActualLogResult(self):
        return com.hpe.amce.mapping.MapperTest.Log.Warn if listAppender.events.invokeMethod("any", [ClosureAnonymousInnerClass(self)]) else com.hpe.amce.mapping.MapperTest.Log.None_

    class ClosureAnonymousInnerClass(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance

        def doCall(self, it):
            return it.loggerName.invokeMethod("startsWith", [invokeMethod("getClass", []).package.name]) and it.level == Level.WARN

        def doCall(self):
            return self.doCall(None)


#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Unroll public Object generate_wanted_behavior_table_to__file()
    def generate_wanted_behavior_table_to__file(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        (File(file)).invokeMethod("withPrintWriter", [ClosureAnonymousInnerClass2(self)]})


    class ClosureAnonymousInnerClass2(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance
            self.index = int(1)

        def doCall(self, writer):
            writer.invokeMethod("println", ["package " + String.invokeMethod("valueOf", [])])
            (list(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Opt, com.hpe.amce.mapping.MapperTest.Get, com.hpe.amce.mapping.MapperTest.Val, com.hpe.amce.mapping.MapperTest.Def, com.hpe.amce.mapping.MapperTest.Tr, com.hpe.amce.mapping.MapperTest.Set, com.hpe.amce.mapping.MapperTest.Fld, com.hpe.amce.mapping.MapperTest.Log))).invokeMethod("each", [ClosureAnonymousInnerClass3(self, DUMMY__1234567890_DUMMYYYYYY___.this, DUMMY__1234567890_DUMMYYYYYY___.this, writer)])
            writer.invokeMethod("println", ["import static " + String.invokeMethod("valueOf", []) + ".cfg"])
            writer.invokeMethod("println", ["class " + String.invokeMethod("valueOf", []) + "Data {\n"])
            index = None
#JAVA TO PYTHON CONVERTER TODO TASK: The following anonymous inner class could not be converted:
#            com.hpe.amce.mapping.MapperTest.Opt.values().invokeMethod("each", new Object[]{new Closure(DUMMY__1234567890_DUMMYYYYYY___.this, DUMMY__1234567890_DUMMYYYYYY___.this)
            #                            {
            #                                public Object doCall(Object optional)
            #                                {
            #                                    return com.hpe.amce.mapping.MapperTest.Get.values().invokeMethod("each", new Object[]{new Closure(DUMMY__1234567890_DUMMYYYYYY___.this, DUMMY__1234567890_DUMMYYYYYY___.this)
            #                                    {
            #                                        public Object doCall(Object getter)
            #                                        {
            #                                            return com.hpe.amce.mapping.MapperTest.Val.values().invokeMethod("each", new Object[]{new Closure(DUMMY__1234567890_DUMMYYYYYY___.this, DUMMY__1234567890_DUMMYYYYYY___.this)
            #                                            {
            #                                                public Object doCall(Object validator)
            #                                                {
            #                                                    return com.hpe.amce.mapping.MapperTest.Def.values().invokeMethod("each", new Object[]{new Closure(DUMMY__1234567890_DUMMYYYYYY___.this, DUMMY__1234567890_DUMMYYYYYY___.this)
            #                                                    {
            #                                                        public Object doCall(Object defaulter)
            #                                                        {
            #                                                            return com.hpe.amce.mapping.MapperTest.Tr.values().invokeMethod("each", new Object[]{new Closure(DUMMY__1234567890_DUMMYYYYYY___.this, DUMMY__1234567890_DUMMYYYYYY___.this)
            #                                                            {
            #                                                                public Object doCall(Object translator)
            #                                                                {
            #                                                                    return com.hpe.amce.mapping.MapperTest.Set.values().invokeMethod("each", new Object[]{new Closure(DUMMY__1234567890_DUMMYYYYYY___.this, DUMMY__1234567890_DUMMYYYYYY___.this)
            #                                                                    {
            #                                                                        public Object doCall(Object setter)
            #                                                                        {
            #                                                                            com.hpe.amce.mapping.MapperTest.Cfg cfg = new com.hpe.amce.mapping.MapperTest.Cfg()
            #                                                                            com.hpe.amce.mapping.MapperTest.Fld field
            #                                                                            com.hpe.amce.mapping.MapperTest.Log log
            #                                                                            if (optional == com.hpe.amce.mapping.MapperTest.Opt.O && getter != com.hpe.amce.mapping.MapperTest.Get.Undef && validator == com.hpe.amce.mapping.MapperTest.Val.Undef && setter == com.hpe.amce.mapping.MapperTest.Set.Undef.asBoolean())
            #                                                                            {
            #                                                                                // For an optional field we have a getter but neither validator nor setter.
            #                                                                                // This means we want to explicitly tell that we'll ignore particular
            #                                                                                // input field - we will not read it and it does not matter if its there or not.
            #                                                                                // Defaulter or translator would be a nonsense.
            #                                                                                field = defaulter == com.hpe.amce.mapping.MapperTest.Def.Undef && translator == com.hpe.amce.mapping.MapperTest.Tr.Undef.asBoolean() ? com.hpe.amce.mapping.MapperTest.Fld.@None : com.hpe.amce.mapping.MapperTest.Fld.CodeErr
            #                                                                            }
            #                                                                            else if (optional == com.hpe.amce.mapping.MapperTest.Opt.O && getter == com.hpe.amce.mapping.MapperTest.Get.Undef && defaulter == com.hpe.amce.mapping.MapperTest.Def.Undef && setter != com.hpe.amce.mapping.MapperTest.Set.Undef.asBoolean())
            #                                                                            {
            #                                                                                // Neither getter, nor defaulter are set for an optional field
            #                                                                                // for which we have a setter.
            #                                                                                // This means we want to explicitly tell that we will ignore this
            #                                                                                // particular output field - we will not provide it.
            #                                                                                // Translator or validator in this mode is nonsense but setter is to be
            #                                                                                // specified to indicate output field that is to be ignored.
            #                                                                                // Since setter will never be called,
            #                                                                                // it does not matter if it will throw or not
            #                                                                                field = validator == com.hpe.amce.mapping.MapperTest.Val.Undef && translator == com.hpe.amce.mapping.MapperTest.Tr.Undef.asBoolean() ? com.hpe.amce.mapping.MapperTest.Fld.@None : com.hpe.amce.mapping.MapperTest.Fld.CodeErr
            #                                                                            }
            #                                                                            else if (getter == com.hpe.amce.mapping.MapperTest.Get.Undef && defaulter == com.hpe.amce.mapping.MapperTest.Def.Undef && optional == com.hpe.amce.mapping.MapperTest.Opt.M.asBoolean())
            #                                                                            {
            #                                                                                // Neither getter, nor defaulter are set for a mandatory field.
            #                                                                                // What will I translate?
            #                                                                                field = com.hpe.amce.mapping.MapperTest.Fld.CodeErr
            #                                                                            }
            #                                                                            else if (setter == com.hpe.amce.mapping.MapperTest.Set.Undef && (validator == com.hpe.amce.mapping.MapperTest.Val.Undef || defaulter != com.hpe.amce.mapping.MapperTest.Def.Undef || translator != com.hpe.amce.mapping.MapperTest.Tr.Undef).asBoolean())
            #                                                                            {
            #                                                                                // If setter is not set then we are in pure checking mode.
            #                                                                                // This is pointless if validator is not set.
            #                                                                                // Also defaulter and translation are useless in this case.
            #                                                                                // To avoid confusing configuration, let's deny it.
            #                                                                                field = com.hpe.amce.mapping.MapperTest.Fld.CodeErr
            #                                                                            }
            #                                                                            else if (getter == com.hpe.amce.mapping.MapperTest.Get.Undef && (validator @in new ArrayList<com.hpe.amce.mapping.MapperTest.Val>(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Val.Ok, com.hpe.amce.mapping.MapperTest.Val.Bad, com.hpe.amce.mapping.MapperTest.Val.Ex)) || translator @in new ArrayList<com.hpe.amce.mapping.MapperTest.Tr>(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Tr.Some, com.hpe.amce.mapping.MapperTest.Tr.Null, com.hpe.amce.mapping.MapperTest.Tr.Ex))).asBoolean())
            #                                                                            {
            #                                                                                // If we have no getter then it's pointless to set validator or translator
            #                                                                                // because they won't be called anyway.
            #                                                                                field = com.hpe.amce.mapping.MapperTest.Fld.CodeErr
            #                                                                            }
            #                     else
            #                                                                            if ((setter == com.hpe.amce.mapping.MapperTest.Set.Ex && shouldSetterBeCalled(cfg)) || (defaulter == com.hpe.amce.mapping.MapperTest.Def.Ex && shouldDefaulterBeCalled(cfg)).asBoolean())
            #                                                                        {
            #                                                                                // Setter deals with translated values -> should not throw.
            #                                                                                // Defaulter must not throw by definition.
            #                                                                                // But we gona know about defaulter only if we had a chance to call it.
            #                                                                                field = com.hpe.amce.mapping.MapperTest.Fld.CodeErr
            #                                                                            }
            #                                                                            else if (optional == com.hpe.amce.mapping.MapperTest.Opt.M && translator == com.hpe.amce.mapping.MapperTest.Tr.Null && shouldTranslatorBeCalled(cfg).asBoolean())
            #                                                                            {
            #                                                                                // If field is mandatory then why translator returns null?
            #                                                                                field = com.hpe.amce.mapping.MapperTest.Fld.CodeErr
            #                                                                            }
            #                                                                            else if (defaulter == com.hpe.amce.mapping.MapperTest.Def.Null && shouldDefaulterBeCalled(cfg).asBoolean())
            #                                                                            {
            #                                                                                // Defaulter returning null makes no sense.
            #                                                                                field = com.hpe.amce.mapping.MapperTest.Fld.CodeErr
            #                                                                            }
            #                                                                            else if (optional == com.hpe.amce.mapping.MapperTest.Opt.M && defaulter == com.hpe.amce.mapping.MapperTest.Def.Undef && (getter @in new ArrayList<com.hpe.amce.mapping.MapperTest.Get>(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Get.Null, com.hpe.amce.mapping.MapperTest.Get.Ex)) || validator @in new ArrayList<com.hpe.amce.mapping.MapperTest.Val>(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Val.Bad, com.hpe.amce.mapping.MapperTest.Val.Ex)) || translator == com.hpe.amce.mapping.MapperTest.Tr.Ex).asBoolean())
            #                                                                            {
            #                                                                                // If defaulter is not set for mandatory field and
            #                                                                                // input is absent, is invalid or we can't translate it
            #                                                                                // then the input is bad.
            #                                                                                field = com.hpe.amce.mapping.MapperTest.Fld.DataErr
            #                                                                            }
            #                     else
            #                                                                            if (optional == com.hpe.amce.mapping.MapperTest.Opt.O && defaulter == com.hpe.amce.mapping.MapperTest.Def.Undef && (getter @in new ArrayList<com.hpe.amce.mapping.MapperTest.Get>(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Get.Null, com.hpe.amce.mapping.MapperTest.Get.Ex)) || validator @in new ArrayList<com.hpe.amce.mapping.MapperTest.Val>(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Val.Bad, com.hpe.amce.mapping.MapperTest.Val.Ex)) || translator == com.hpe.amce.mapping.MapperTest.Tr.Ex).asBoolean())
            #                                                                            {
            #                                                                                // If defaulter is not set for optional field and
            #                                                                                // input is absent, is invalid or we can't translate it
            #                                                                                // then we just skip the field.
            #                                                                                field = com.hpe.amce.mapping.MapperTest.Fld.@None
            #                                                                            }
            #                     else if (shouldDefaulterBeCalled(cfg) && setter == com.hpe.amce.mapping.MapperTest.Set.Ok.asBoolean())
            #                     {
            #                                                                                // Default value is used if anything bad happens.
            #                                                                                field = com.hpe.amce.mapping.MapperTest.Fld.Def
            #                                                                            }
            #                                                                            else if (getter == com.hpe.amce.mapping.MapperTest.Get.Some && validator @in new ArrayList<com.hpe.amce.mapping.MapperTest.Val>(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Val.Undef, com.hpe.amce.mapping.MapperTest.Val.Ok)) && translator @in new ArrayList<com.hpe.amce.mapping.MapperTest.Tr>(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Tr.Some, com.hpe.amce.mapping.MapperTest.Tr.Null)) && setter == com.hpe.amce.mapping.MapperTest.Set.Ok.asBoolean())
            #                                                                            {
            #                                                                                // If everything is ok then translated value is used.
            #                                                                                field = com.hpe.amce.mapping.MapperTest.Fld.Tr
            #                                                                            }
            #                     else if (getter == com.hpe.amce.mapping.MapperTest.Get.Some && validator @in new ArrayList<com.hpe.amce.mapping.MapperTest.Val>(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Val.Undef, com.hpe.amce.mapping.MapperTest.Val.Ok)) && translator == com.hpe.amce.mapping.MapperTest.Tr.Undef && setter == com.hpe.amce.mapping.MapperTest.Set.Ok.asBoolean())
            #                                                                            {
            #                                                                                // Original value is used if everything is ok but translator is not set.
            #                                                                                // This is when we copy value as is.
            #                                                                                field = com.hpe.amce.mapping.MapperTest.Fld.Orig
            #                                                                            }
            #                     else
            #                                                                            if (getter == com.hpe.amce.mapping.MapperTest.Get.Some && validator == com.hpe.amce.mapping.MapperTest.Val.Ok && setter == com.hpe.amce.mapping.MapperTest.Set.Undef.asBoolean())
            #                                                                        {
            #                                                                                // Pure validation success scenario.
            #                                                                                field = com.hpe.amce.mapping.MapperTest.Fld.@None
            #                                                                            }
            #                                                                            else if (getter == com.hpe.amce.mapping.MapperTest.Get.Undef && validator == com.hpe.amce.mapping.MapperTest.Val.Undef && translator == com.hpe.amce.mapping.MapperTest.Tr.Undef && defaulter @in new ArrayList<com.hpe.amce.mapping.MapperTest.Def>(java.util.Arrays.asList(com.hpe.amce.mapping.MapperTest.Def.Some, com.hpe.amce.mapping.MapperTest.Def.Null)) && setter == com.hpe.amce.mapping.MapperTest.Set.Ok.asBoolean())
            #                                                                            {
            #                                                                                // Always set a field to a constant value when no input field.
            #                                                                                field = com.hpe.amce.mapping.MapperTest.Fld.Def
            #                                                                            }
            #                     else
            #                     {
            #                                                                                throw new IllegalStateException("Don\'t know expected result for " + String.invokeMethod("valueOf", new Object[]{cfg}))
            #                                                                            }
            #
            #                                                                            log = shouldWarn(cfg) ? com.hpe.amce.mapping.MapperTest.Log.Warn : com.hpe.amce.mapping.MapperTest.Log.@None
            #                                                                            return writer.invokeMethod("println", new Object[]{"def l" + String.invokeMethod("valueOf", new Object[]{index++}) + "(){cfg(" + "Opt." + String.invokeMethod("valueOf", new Object[]{optional}) + ", Get." + String.invokeMethod("valueOf", new Object[]{getter}) + ", Val." + String.invokeMethod("valueOf", new Object[]{validator}) + ", Def." + String.invokeMethod("valueOf", new Object[]{defaulter}) + ", Tr." + String.invokeMethod("valueOf", new Object[]{translator}) + ", Set." + String.invokeMethod("valueOf", new Object[]{setter}) + ", Fld." + String.invokeMethod("valueOf", new Object[]{field}) + ", Log." + String.invokeMethod("valueOf", new Object[]{log}) + ")}"})
            #                                                                        }
            #
            #                                                                    }
            #                                                                }
            #                                                                )
            #                                                                }
            #
            #                                                            }
            #                                                    }
            #                                                    )
            #                                                        }
            #
            #                                                    }
            #                                        }
            #                                        )
            #                                                }
            #
            #                                            }
            #                            }
            )

        class ClosureAnonymousInnerClass3(Closure):


            def __init__(self, outerInstance, self, self, writer):
                super().__init__(self, self)
                self._outerInstance = outerInstance
                self._writer = writer

            def doCall(self, it):
                return self._writer.invokeMethod("println", ["import " + String.invokeMethod("valueOf", []) + " as " + String.invokeMethod("valueOf", [])])

            def doCall(self):
                return self.doCall(None)


#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
);
return writer.invokeMethod("println", ["\n}"])
}

}
}
)

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#then:
True

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#where:
file | _
return DATA_PATH | _
}

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Unroll public void auto_for__loadedConfig_should_be__loadedDesiredBehaviour()
public void auto_for__loadedConfig_should_be__loadedDesiredBehaviour()
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    given:
    config = loadedConfig
    desiredBehaviour = loadedDesiredBehaviour
    fieldResult = AtomicReference(com.hpe.amce.mapping.MapperTest.Fld.None_)
    mappingContext = MappingContext("original", "result", list(java.util.Arrays.asList("param1", "param2")))
    mapper = cfgToMapper(config, fieldResult)

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    when:
    try:
        (MandatoryFieldMapper()).invokeMethod("mapField", [mapper, mappingContext]) if config.getOptional() == com.hpe.amce.mapping.MapperTest.Opt.M.asBoolean() else (OptionalFieldMapper()).invokeMethod("mapField", [mapper, mappingContext])
    except IllegalArgumentException as e:
        fieldResult.invokeMethod("set", [com.hpe.amce.mapping.MapperTest.Fld.DataErr])
    except IllegalStateException as e:
        fieldResult.invokeMethod("set", [com.hpe.amce.mapping.MapperTest.Fld.CodeErr])


#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    then:
    fieldResult.invokeMethod("get", []) == desiredBehaviour.getFieldResult()
    getActualLogResult() == desiredBehaviour.getLogResult()

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    where:
    list(java.util.Arrays.asList(loadedConfig, loadedDesiredBehaviour)) << com.hpe.amce.mapping._loadTable(DATA_PATH)

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Unroll public Object manual_for__config_should_be__desiredBehaviour()
public Object self.manual_for__config_should_be__desiredBehaviour()
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    given:
    fieldResult = AtomicReference(com.hpe.amce.mapping.MapperTest.Fld.None_)
    mappingContext = MappingContext("original object", "result object", list(java.util.Arrays.asList("param1", "param2")))
    mapper = cfgToMapper(config, fieldResult)

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    when:
    try:
        (MandatoryFieldMapper()).invokeMethod("mapField", [mapper, mappingContext]) if config.getOptional() == com.hpe.amce.mapping.MapperTest.Opt.M.asBoolean() else (OptionalFieldMapper()).invokeMethod("mapField", [mapper, mappingContext])
    except IllegalArgumentException as e:
        fieldResult.invokeMethod("set", [com.hpe.amce.mapping.MapperTest.Fld.DataErr])
    except IllegalStateException as e:
        fieldResult.invokeMethod("set", [com.hpe.amce.mapping.MapperTest.Fld.CodeErr])


#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    then:
    fieldResult.invokeMethod("get", []) == desiredBehaviour.fieldResult
    getActualLogResult() == desiredBehaviour.logResult

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    where:
    config | desiredBehaviour
    return com.hpe.amce.mapping.MapperTest.Cfg() | com.hpe.amce.mapping.MapperTest.Behaviuor()

public Boolean self.closures_have_access_to_context_and_parameters()
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    given:
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final Reference<Boolean> getterOk = new groovy.lang.Reference<boolean>((boolean) false);
    getterOk = groovy.lang.Reference(bool(False))
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final Reference<Boolean> validatorOk = new groovy.lang.Reference<boolean>((boolean) false);
    validatorOk = groovy.lang.Reference(bool(False))
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final Reference<Boolean> translatorOk = new groovy.lang.Reference<boolean>((boolean) false);
    translatorOk = groovy.lang.Reference(bool(False))
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final Reference<Boolean> setterOk = new groovy.lang.Reference<boolean>((boolean) false);
    setterOk = groovy.lang.Reference(bool(False))
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final Reference<Boolean> defaulterOk = new groovy.lang.Reference<boolean>((boolean) false);

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
