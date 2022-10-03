//====================================================================================================
//The Free Edition of Java to Python Converter limits conversion output to 100 lines per file.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================

class MapperTestData(GroovyObjectSupport):
    def l1(self):
        return invokeMethod("cfg", [Opt.M, Get.Some, Val.Ok, Def.Some, Tr.Some, Set.Ok, Fld.Tr, Log.None_])

    class ClosureAnonymousInnerClass2(Closure):


        def __init__(self, outerInstance, self, self, translatorOk):
            super().__init__(self, self)
            self.outerInstance = outerInstance
            self.translatorOk = translatorOk

        def doCall(self, it):
            assert parameters.getAt(0) == "param"
            assert originalObject.getAt("a") == "b"
            assert resultObject.getAt("x") == "y"
            assert it is "b"
            if not translatorOk.get().asBoolean():
                translatorOk.set(True)
                raise NullPointerException("Let's branch to defaulter")
            else:
                return "c" # Just to avoid lots of idea highlighting


        def doCall(self):
            return doCall(None)


    class ClosureAnonymousInnerClass3(Closure):


        def __init__(self, outerInstance, self, self, defaulterOk):
            super().__init__(self, self)
            self.outerInstance = outerInstance
            self.defaulterOk = defaulterOk

        def doCall(self, it):
            assert parameters.getAt(0) == "param"
            assert originalObject.getAt("a") == "b"
            assert resultObject.getAt("x") == "y"
            defaulterOk.set(True)
            return "d"

        def doCall(self):
            return doCall(None)


    class ClosureAnonymousInnerClass4(Closure):


        def __init__(self, outerInstance, self, self, setterOk):
            super().__init__(self, self)
            self.outerInstance = outerInstance
            self.setterOk = setterOk

        def doCall(self, it):
            assert parameters.getAt(0) == "param"
            assert originalObject.getAt("a") == "b"
            assert resultObject.getAt("x") == "y"
            assert it is "d"
            resultObject["a"] = it
            return com.hpe.amce.mapping.MapperTestData._setGroovyRef(setterOk, True)

        def doCall(self):
            return doCall(None)


    class ClosureAnonymousInnerClass5(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, it):
            return java.util.regex.Pattern.compile(/\s * def_. + cfg\(. +\)/).matcher(it)

        def doCall(self):
            return doCall(None)


    class ClosureAnonymousInnerClass7(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, it):
            return it.invokeMethod("replaceAll", [/\)]/,"" })

        def doCall(self):
            return doCall(None)


    class ClosureAnonymousInnerClass8(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, it):
            return it.invokeMethod("replaceAll", [/\w +\. (\w +)/, /$1 /])

        def doCall(self):
            return doCall(None)


    class ClosureAnonymousInnerClass9(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, it):
            return it.invokeMethod("split", [/, /]).invokeMethod("trim", [])

        def doCall(self):
            return doCall(None)


    class ClosureAnonymousInnerClass10(Closure):

        def __init__(self, outerInstance):
            super().__init__(outerInstance, outerInstance)
            self.outerInstance = outerInstance

        def doCall(self, it):
            i = int(0)
            return [com.hpe.amce.mapping.MapperTest.Cfg(), com.hpe.amce.mapping.MapperTest.Behaviuor()]

        def doCall(self):
            return doCall(None)


    class ClosureAnonymousInnerClass12(Closure):

        def __init__(self, outerInstance, self, self):
            super().__init__(self, self)
            self.outerInstance = outerInstance

        def doCall(self, it):
            return True

        def doCall(self):
            return doCall(None)


    class ClosureAnonymousInnerClass13(Closure):

        def __init__(self, outerInstance, self, self):
            super().__init__(self, self)
            self.outerInstance = outerInstance


//====================================================================================================
//End of the allowed output for the Free Edition of Java to Python Converter.

//To purchase the Premium Edition, visit our website:
//https://www.tangiblesoftwaresolutions.com/order/order-java-to-python.html
//====================================================================================================
