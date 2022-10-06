#*
# * Descriptor of a field mapping.
# * <p>
# * Intended to be constructed using fluid API and method chaining.
# * Example:
# * <code><pre>
# *     new Field&lt;Map&lt;String,?&gt;,Event,String,Long&gt;().
# *         withId('notificationIdentifier').
# *         withGetter {it.identifier}.
# *         withTranslator {Long.parseLong(it)}.
# *         withSetter { resultObject.notificationIdentifier=it }* </pre></code>
# * <p>
# * OO - Original object type.
# * RO - Resulting object type.
# * OF - Original field type.
# * RF - Resulting field type.
# * P - Type of parameters object.
# 
from typing import Generic, TypeVar, Callable

OO = TypeVar('OO')
RO = TypeVar('RO')
OF = TypeVar('OF')
RF = TypeVar('RF')
P = TypeVar('P')

class Field(Generic[OO, RO, OF, RF, P]):

    #     * Identifier of field.
    #     * Used for debugging and testing purposes.
    #
    #     * Gets field value from original object.
    #
    #     * Verifies field value from original object.
    #
    #     * Translates field value from original object to format of result object.
    #
    #     * Injects translated field value into result object.
    #
    #     * Gets field value in case it was not set in original object.
    #
    def __init__(self, withId: str=None,
                 withGetter: Callable[[OO], OF]=None,
                 withValidator: Callable[[OF], bool]=None,
                 withTranslator: Callable[[OF], RF]=None,
                 withSetter: Callable[[RF], None]=None,
                 withDefaulter: Callable[[], RF]=None
                 ):
        self.id: str = withId
        self.getter = withGetter
        self.validator = withValidator
        self.translator = withTranslator
        self.setter = withSetter
        self.defaulter = withDefaulter
        print(self.__str__())


    def __str__(self) -> str:
        import inspect
        result = self.id
        for key, _lambda in {"G":self.getter, "D":self.defaulter, "T":self.translator, "V":self.validator, "S":self.setter}.items():
            if _lambda:
                result += f" {key}=~{inspect.getsource(_lambda).split(sep='lambda')[1].split(sep=':')[1].strip()}~"
        return result

