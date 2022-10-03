#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class Groovy307CompileStaticTest extends Specification
class Groovy307CompileStaticTest(Specification):

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self._charset = StandardCharsets.UTF_8.invokeMethod("name", [])
        map = LinkedHashMap(1)
        map.put((com.hpe.amce.mapping.Groovy307CompileStaticTest.F()).invokeMethod("withId", ["CONTENT_TYPE"]).invokeMethod("withDefaulter", {Closure(self, self)
        public String self.doCall(Object it)
        return self.getCharset()
    
        public String self.doCall()
        return self.doCall(None)
    

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileDynamic public Boolean mapping_works()
    def mapping_works(self):
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        given:
        exchange = invokeMethod("Mock", [])
        mapper = SimpleObjectMapper()
        input = com.hpe.amce.mapping.Groovy307CompileStaticTest.ReplyEms(exchange)
        output = com.hpe.amce.mapping.Groovy307CompileStaticTest.ReplyBus()
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        when:
        mapper.invokeMethod("mapAllFields", [input, output, self.getMapping(), exchange])
#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java labels and gotos:
#        then:
        1 * exchange.invokeMethod("setExchangeProperty", ["charset", self.getCharset()])
        map = LinkedHashMap(1)
        map.put("Content-Type", "application/json; charset=UTF-8")
        return output.getHeaders() is map

    def getCharset(self):
        return self._charset

    def setCharset(self, charset):
        self._charset = charset

    def getMapping(self):
        return mapping

    def setMapping(self, mapping):
        self.mapping = mapping


#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
    ).invokeMethod("withSetter", new Object[]{new Closure(self, self)
        def doCall(self, it):
            parameters.invokeMethod("setExchangeProperty", ["charset", self.getCharset()])
            # The following form does not work in Groovy 3.0.7
            # resultObject.headers['Content-Type']=
            #         "application/json; charset=$charset".toString()
            # However, this one works
            return resultObject.headers.invokeMethod("put", ["Content-Type", "application/json; charset=" + String.invokeMethod("valueOf", []).invokeMethod("toString", [])])

        def doCall(self):
            return self.doCall(None)

#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
), True);
self._mapping = map
}

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull private Map<Field<com.hpe.amce.mapping.Groovy307CompileStaticTest.ReplyEms, com.hpe.amce.mapping.Groovy307CompileStaticTest.ReplyBus, ?, ?, Exchange>, Boolean> mapping;
private Map<Field<com.hpe.amce.mapping.Groovy307CompileStaticTest.ReplyEms, com.hpe.amce.mapping.Groovy307CompileStaticTest.ReplyBus, Exchange>, Boolean> self._mapping

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @ToString(includeNames = true, includePackage = false) private static class ReplyEms extends GroovyObjectSupport
private static class ReplyEms extends GroovyObjectSupport
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: public ReplyEms(@Nonnull Exchange exchange)
    public ReplyEms( Exchange exchange)
        headers = ((LinkedHashMap()))
        body = ((LinkedHashMap()))

    public Map<String, Object> getHeaders()
        return headers

    public void setHeaders(Map<String, Object> headers)
        self.headers = headers

    public Map<String, Object> getBody()
        return body

    public void setBody(Map<String, Object> body)
        self.body = body

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull private Map<String, Object> headers;
    private Map<String, Object> headers
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull private Map<String, Object> body;
    private Map<String, Object> body

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @ToString(includeNames = true, includePackage = false) private static class ReplyBus extends GroovyObjectSupport
private static class ReplyBus extends GroovyObjectSupport
    public Map<String, Object> getHeaders()
        return headers

    public void setHeaders(Map<String, Object> headers)
        self.headers = headers

    public Map<String, Object> getBody()
        return body

    public void setBody(Map<String, Object> body)
        self.body = body

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull private Map<String, Object> headers = new LinkedHashMap();
    private Map<String, Object> headers = LinkedHashMap()
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull private Map<String, Object> body = new LinkedHashMap();
    private Map<String, Object> body = LinkedHashMap()

#    *
#     * A field with pre-set types of original and result objects for reply mapping.
#     * OF - Type of original field.
#     * RF - Type of result field.
#     
private static class F<OF, RF> extends Field<com.hpe.amce.mapping.Groovy307CompileStaticTest.ReplyEms, com.hpe.amce.mapping.Groovy307CompileStaticTest.ReplyBus, OF, RF, Exchange>

private static <T> T com.hpe.amce.mapping._setGroovyRef(groovy.lang.Reference<T> ref, T newValue)
    ref.set(newValue)
    return newValue
}
