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
from typing import Generic, TypeVar, Callable, Any, Self

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

        """
        `withId`: Sets identifier of field
        
        :param id: The id of the field. This is used for debugging and testing purposes
        :type id: str
        :return: self for chaining
        """
    def withId(self, id: str) -> Self:
        self.id = id
        return self

        """
        Sets getter of value from original object
        
        :param c: Closure that takes one parameter - original object. Should return original field value
        """
    def withGetter(self, c: Callable[[OO], OF]) -> Self:
        self.getter = c
        return self

    #    *
    #     * Sets validator for original value.
    #     *
    #     * @param c Closure that takes one parameter - original field value.
    #     *          Should return true if original value has acceptable value.
    #     * @return this for chaining
    #     
    def withValidator(self, c: Callable[[OF], bool]) -> Self:
        self.validator = c
        return self

    #    *
    #     * Sets mapper from original field value to resulting field value.
    #     *
    #     * @param c Closure that takes one parameter - original field value.
    #     *          Additional translator parameters are available via closure delegate.
    #     *          Should return resulting mapped value.
    #     * @return this for chaining
    #     
    def withTranslator(self, c: Callable[[OF], RF]) -> Self:
        self.translator = c
        return self

    #    *
    #     * Sets setter for resulting field.
    #     *
    #     * @param c Closure that takes one parameter - resulting field value.
    #     *          Resulting object can be taken from delegate as {@link MappingContext#resultObject}.
    #     *          Doesn't have to return anything.
    #     * @return this for chaining
    #     
    def withSetter(self, c: Callable[[RF], None]) -> Self:
        self.setter = c
        return self

    #    *
    #     * Sets calculator of default value.
    #     *
    #     * @param c Closure that takes no parameters and returns resulting value for the field.
    #     * @return this for chaining.
    #     
    def withDefaulter(self, c: Callable[[], RF]) -> Self:
        self.defaulter = c
        return self

    def toString(self) -> str:
        return self.id

