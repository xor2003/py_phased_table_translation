class AbstractStateMachineFieldMapperTest(Specification):
    def error_when_Neither_getter_not_defaulter_are_set___no_way_to_obtain_value_to_validate_translate_set(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        mapper.invokeMethod("mapField", {(Field()).invokeMethod("withValidator", [ClosureAnonymousInnerClass(self)]).invokeMethod("withSetter", {Closure(self, self){public void doCall(Object it){}public void doCall(){doCall(None)

    class ClosureAnonymousInnerClass(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self._outerInstance = outerInstance

        def doCall(self, it):
            return True

        def doCall(self):
            return self.doCall(None)


}
), None
}
)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#then:
invokeMethod("thrown", [Exception])
}

public void error_If_setter_is_not_set_this_means_we_are_in_pure_checking_mode__________This_is_pointless_if_validator_is_not_set__________Also_defaulter_and_translation_are_useless_in_this_case_and_should_not_be_set_()
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    when:
    self._mapper.invokeMethod("mapField", [(Field()).invokeMethod("withGetter", []), None])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    then:
    invokeMethod("thrown", [Exception])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    when:
    self._mapper.invokeMethod("mapField", {(Field()).invokeMethod("withGetter", [ClosureAnonymousInnerClass2(self)]).invokeMethod("withValidator", {Closure(self, self){public Boolean self.doCall(Object it){return True

public Boolean self.doCall()
    return self.doCall(None)

}
}
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
).invokeMethod("withDefaulter", new Object[]{new Closure(self, self)
    public void self.doCall(Object it)

    public void self.doCall()
        self.doCall(None)

}
), None
}
)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#then:
invokeMethod("thrown", [Exception])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#when:
self._mapper.invokeMethod("mapField", {(Field()).invokeMethod("withGetter", [ClosureAnonymousInnerClass4(self)]).invokeMethod("withValidator", {Closure(self, self){public Boolean self.doCall(Object it){return True
}

public Boolean self.doCall()
    return self.doCall(None)

}
}
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
).invokeMethod("withTranslator", new Object[]{new Closure(self, self)
    public void self.doCall(Object it)

    public void self.doCall()
        self.doCall(None)

}
), None
}
)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#then:
invokeMethod("thrown", [Exception])
}

public void If_there_is_no_getter_then_it_s_pointless_to_set_________validator_or_translator_because_they_won_t_be_called_anyway_()
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    when:
    self._mapper.invokeMethod("mapField", {(Field()).invokeMethod("withValidator", [ClosureAnonymousInnerClass6(self)]).invokeMethod("withDefaulter", {Closure(self, self){public void self.doCall(Object it){}public void self.doCall(){self.doCall(None)

}
}
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
).invokeMethod("withSetter", new Object[]{new Closure(self, self)
    public void self.doCall(Object it)

    public void self.doCall()
        self.doCall(None)

}
), None
}
)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#then:
invokeMethod("thrown", [Exception])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#when:
self._mapper.invokeMethod("mapField", {(Field()).invokeMethod("withTranslator", [ClosureAnonymousInnerClass8(self)]).invokeMethod("withDefaulter", {Closure(self, self){public void self.doCall(Object it){}public void self.doCall(){self.doCall(None)
}

}
}
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
).invokeMethod("withSetter", new Object[]{new Closure(self, self)
    public void self.doCall(Object it)

    public void self.doCall()
        self.doCall(None)

}
), None
}
)
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#then:
invokeMethod("thrown", [Exception])
}

public Object self.as_is_from_source_is_ok_and_delegates_to_child_machine()
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    given:
    stateMachine = invokeMethod("Mock", [])
    field = (Field()).invokeMethod("withGetter", [ClosureAnonymousInnerClass10(self)]).invokeMethod("withSetter", {Closure(self, self){public void self.doCall(Object it){}public void self.doCall(){self.doCall(None)

}
}
)
mappingContext = invokeMethod("Mock", [])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#when:
self._mapper.invokeMethod("mapField", [field, mappingContext])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#then:
1 * self._mapper.invokeMethod("getStateMachine", [field]) >> self._stateMachine
return 1 * self._stateMachine.invokeMethod("process", [field, mappingContext, (not None)])
}

public Object self.fixed_value_is_ok_and_delegates_to_child_machine()
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    given:
    stateMachine = invokeMethod("Mock", [])
    field = (Field()).invokeMethod("withDefaulter", [ClosureAnonymousInnerClass11(self)]).invokeMethod("withSetter", {Closure(self, self){public void self.doCall(Object it){}public void self.doCall(){self.doCall(None)

}
}
)
mappingContext = invokeMethod("Mock", [])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#when:
self._mapper.invokeMethod("mapField", [field, mappingContext])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#then:
1 * self._mapper.invokeMethod("getStateMachine", [field]) >> self._stateMachine
return 1 * self._stateMachine.invokeMethod("process", [field, mappingContext, (not None)])
}

public Object self.pure_checking_is_ok_and_delegates_to_child_machine()
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#    given:
    stateMachine = invokeMethod("Mock", [])
    field = (Field()).invokeMethod("withGetter", [ClosureAnonymousInnerClass12(self)]).invokeMethod("withValidator", {Closure(self, self){public Boolean self.doCall(Object it){return True

public Boolean self.doCall()
    return self.doCall(None)

}
}
)
mappingContext = invokeMethod("Mock", [])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#when:
self._mapper.invokeMethod("mapField", [field, mappingContext])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#then:
1 * self._mapper.invokeMethod("getStateMachine", [field]) >> self._stateMachine
return 1 * self._stateMachine.invokeMethod("process", [field, mappingContext, (not None)])
}

public AbstractStateMachineFieldMapper self.getMapper()
    return self._mapper

public void setMapper(AbstractStateMachineFieldMapper self._mapper)
    self._mapper = self._mapper

private AbstractStateMachineFieldMapper self._mapper = invokeMethod("Spy", [])
}
