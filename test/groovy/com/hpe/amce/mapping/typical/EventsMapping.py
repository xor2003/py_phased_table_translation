//====================================================================================================
//The Free Edition of Java to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================

#*
# * Translates notifications.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class EventsMapping extends GroovyObjectSupport
class EventsMapping(GroovyObjectSupport):

    def __init__(self):
        #instance fields found by Java to Python Converter:
        map = LinkedHashMap(20)
        map.put((com.hpe.amce.mapping.typical.EventsMapping.F()).invokeMethod("withId", ["notificationType"]).invokeMethod("withDefaulter", {Closure(self, self)
        public String self.doCall(Object it)
        return "notifyNewAlarm"
    
        public String self.doCall()
        return self.doCall(None)
    

    #    *
    #     * Maps single real time event.
    #     *
    #     * @param raw          Incoming event.
    #     * @param batchContext Mapping context.
    #     * @return List of outgoing mapped events.
    #     
    def mapEvent(self, raw, batchContext):
        notificationType = "notifyNewAlarm"
        map = LinkedHashMap(1)
        map.put("raw", Object.invokeMethod("cast", [raw]))
        event = map
        eventContext = com.hpe.amce.mapping.typical.EventsMapping.EventContext(batchContext, notificationType)
        mapper.invokeMethod("mapAllFields", [raw, event, self.getNotifyNewAlarm(), eventContext])
        result = Collections.invokeMethod("singletonList", [Map.invokeMethod("cast", [])])
        return result

    def getNotifyNewAlarm(self):
        return notifyNewAlarm

    def setNotifyNewAlarm(self, notifyNewAlarm):
        self.notifyNewAlarm = notifyNewAlarm

    def getConfiguredAgentEntity(self):
        return configuredAgentEntity

    def setConfiguredAgentEntity(self, configuredAgentEntity):
        self.configuredAgentEntity = configuredAgentEntity

    def getProbableCauses(self):
        return probableCauses

    def setProbableCauses(self, probableCauses):
        self.probableCauses = probableCauses

    def getAlarmTypes(self):
        return alarmTypes

    def setAlarmTypes(self, alarmTypes):
        self.alarmTypes = alarmTypes

    def getSeverities(self):
        return severities

    def setSeverities(self, severities):
        self.severities = severities

    def getRtObjectInstanceFields(self):
        return rtObjectInstanceFields

    def getDistinguishedNameSerializer(self):
        return distinguishedNameSerializer

    def setDistinguishedNameSerializer(self, distinguishedNameSerializer):
        self.distinguishedNameSerializer = distinguishedNameSerializer

    def getTimeSerializer(self):
        return timeSerializer

    def setTimeSerializer(self, timeSerializer):
        self.timeSerializer = timeSerializer

    def getMapper(self):
        return mapper

    def setMapper(self, mapper):
        self.mapper = mapper

    #    *
    #     * Mapping table for raise alarm notifications.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
    ).invokeMethod("withSetter", new Object[]{new Closure(self, self)
        def doCall(self, it):
            return resultObject["out_notificationType"] = it

        def doCall(self):
            return self.doCall(None)

#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
), True);
#JAVA TO PYTHON CONVERTER TODO TASK: The following assignment within expression was not converted by Java to Python Converter:
#ORIGINAL LINE: map.put(new com.hpe.amce.mapping.typical.EventsMapping.F<Void, String>().invokeMethod("withId", new Object[]{"agentEntity"}).invokeMethod("withDefaulter", new Object[]{new Closure(this, this)
map.put((com.hpe.amce.mapping.typical.EventsMapping.F()).invokeMethod("withId", ["agentEntity"]).invokeMethod("withDefaulter", [ClosureAnonymousInnerClass()]).invokeMethod("withSetter", {Closure(self, self){public Object self.doCall(Object it){return resultObject["out_agentEntity"] = it
}

public Object self.doCall()
    return self.doCall(None)

}
}
), True)
map.put((com.hpe.amce.mapping.typical.EventsMapping.F()).invokeMethod("withId", ["alarmId"]).invokeMethod("withGetter", [ClosureAnonymousInnerClass2(self)]).invokeMethod("withValidator", [Closure.IDENTITY]).invokeMethod("withTranslator", {Closure(self, self){public Object self.doCall(Object it){return it
}

public Object self.doCall()
    return self.doCall(None)

}
}
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
).invokeMethod("withSetter", new Object[]{new Closure(self, self)
    public Object self.doCall(Object it)
        return resultObject["out_alarmId"] = it

    public Object self.doCall()
        return self.doCall(None)

}
), True)
map.put((com.hpe.amce.mapping.typical.EventsMapping.F()).invokeMethod("withId", ["alarmType"]).invokeMethod("withGetter", [ClosureAnonymousInnerClass4(self)]).invokeMethod("withValidator", {Closure(self, self){public Object self.doCall(Object it){return getAlarmTypes().invokeMethod("containsKey", [it])
}

public Object self.doCall()
    return self.doCall(None)

}
}
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
).invokeMethod("withTranslator", new Object[]{new Closure(self, self)
    public Object self.doCall(Object it)
        return getAlarmTypes().getAt(it)

    public Object self.doCall()
        return self.doCall(None)

}
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
).invokeMethod("withSetter", new Object[]{new Closure(self, self)
    public Object self.doCall(Object it)
        return resultObject["out_alarmType"] = it

    public Object self.doCall()
        return self.doCall(None)

}
), True)
#JAVA TO PYTHON CONVERTER TODO TASK: The following assignment within expression was not converted by Java to Python Converter:
#ORIGINAL LINE: map.put(new com.hpe.amce.mapping.typical.EventsMapping.F<String, String>().invokeMethod("withId", new Object[]{"objectClass"}).invokeMethod("withGetter", new Object[]{new Closure(this, this)
map.put((com.hpe.amce.mapping.typical.EventsMapping.F()).invokeMethod("withId", ["objectClass"]).invokeMethod("withGetter", [ClosureAnonymousInnerClass7(self)]).invokeMethod("withSetter", {Closure(self, self){public Object self.doCall(Object it){return resultObject["out_objectClass"] = it
}

public Object self.doCall()
    return self.doCall(None)

}
}
), False)
map.put((com.hpe.amce.mapping.typical.EventsMapping.F()).invokeMethod("withId", ["objectInstance"]).invokeMethod("withGetter", {ClosureAnonymousInnerClass8(self)public Object self.doCall(){return self.doCall(None)

}

}
}
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
).invokeMethod("withValidator", new Object[]{new Closure(self, self)
    public Boolean self.doCall(Object it)
        return (it.getAt("in)CLASS_2") and it.getAt("in_CLASS_1")) or it.getAt("in_objectInstance")

    public Boolean self.doCall()
        return self.doCall(None)

}
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
).invokeMethod("withTranslator", new Object[]{new Closure(self, self)
    public String self.doCall(Object it)
#JAVA TO PYTHON CONVERTER WARNING: The original Java variable was marked 'final':
#ORIGINAL LINE: final String s = (String) it.getAt("in_objectInstance");
        s = str(it.getAt("in_objectInstance"))
        map1 = LinkedHashMap(2)
        map1.put("CLASS_1", it.getAt("in_CLASS_1"))
        map1.put("CLASS_2", it.getAt("in_CLASS_2"))

//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
