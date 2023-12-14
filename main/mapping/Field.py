# pylint: disable=invalid-name
import logging
from typing import Generic, TypeVar, Callable, Optional

logger = logging.getLogger(__name__)

OO = TypeVar("OO")
RO = TypeVar("RO")
OF = TypeVar("OF")
RF = TypeVar("RF")
P = TypeVar("P")


class Field(Generic[OO, RO, OF, RF, P]):
    """Descriptor of a field mapping.

    Intended to be constructed using fluid API and method chaining.

    Example:
    -------
    <code><pre>
        new Field&lt;Map&lt;String,?&gt;,Event,String,Long&gt;().
            withId('notificationIdentifier').
            withGetter {it.identifier}.
            withTranslator {Long.parseLong(it)}.
            withSetter { resultObject.notificationIdentifier=it }* </pre></code>

    OO - Original object type.
    RO - Resulting object type.
    OF - Original field type.
    RF - Resulting field type.

    P - Type of parameters object.
    """

    def __init__(
            self,
            *,
            withId: str,
            withGetter: Optional[Callable[[OO], OF]] = None,
            withValidator: Optional[Callable[[OF], bool]] = None,
            withTranslator: Optional[Callable[[OF], RF]] = None,
            withSetter: Optional[Callable[[RF], None]] = None,
            withDefaulter: Optional[Callable[[], RF]] = None,
    ):
        """:param withId:         Identifier of field.
                               Used for debugging and testing purposes.
        :param withGetter:     Gets field value from original object.
        :param withValidator:  Verifies field value from original object.
        :param withTranslator: Translates field value from original object to format of result object.
        :param withSetter:     Injects translated field value into result object.
        :param withDefaulter:  Gets field value in case it was not set in original object.
        """
        self.id = withId
        self.getter = withGetter
        self.validator = withValidator
        self.translator = withTranslator
        self.setter = withSetter
        self.defaulter = withDefaulter
        logger.debug(self)


    def withId(self, id: str) -> 'Field':
        """
        Sets identifier of field.

        Args:
            id (str): Identifier for debugging and testing purposes.

        Returns:
            Field: This instance for chaining.
        """
        self.id = id
        return self

    def withGetter(self, c: Callable[[OO], OF]) -> 'Field':
        """
        Sets getter of value from original object.

        Args:
            c (Callable[[OO], OF]): Closure that takes one parameter - original object.
                                    Should return original field value.

        Returns:
            Field: This instance for chaining.
        """
        self.getter = c
        return self

    def withValidator(self, c: Callable[[OF], bool]) -> 'Field':
        """
        Sets validator for original value.

        Args:
            c (Callable[[OF], bool]): Closure that takes one parameter - original field value.
                                        Should return true if original value has acceptable value.

        Returns:
            Field: This instance for chaining.
        """
        self.validator = c
        return self

    def withTranslator(self, c: Callable[[OF], RF]) -> 'Field':
        """
        Sets mapper from original field value to resulting field value.

        Args:
            c (Callable[[OF], RF]): Closure that takes one parameter - original field value.
                                    Additional translator parameters are available via closure delegate.
                                    Should return resulting mapped value.

        Returns:
            Field: This instance for chaining.
        """
        self.translator = c
        return self

    def withSetter(self, c: Callable[[RF], None]) -> 'Field':
        """
        Sets setter for resulting field.

        Args:
            c (Callable[[RF], None]): Closure that takes one parameter - resulting field value.
                                        Resulting object can be taken from delegate as {@link MappingContext#resultObject}.
                                        Doesn't have to return anything.

        Returns:
            Field: This instance for chaining.
        """
        self.setter = c
        return self

    def withDefaulter(self, c: Callable[[], RF]) -> 'Field':
        """
        Sets calculator of default value.

        Args:
            c (Callable[[], RF]): Closure that takes no parameters and returns resulting value for the field.

        Returns:
            Field: This instance for chaining.
        """
        self.defaulter = c
        return self

    def __str__(self) -> str:
        from inspect import getsource

        result = self.id
        for key, _lambda in {
            "G": self.getter,
            "D": self.defaulter,
            "T": self.translator,
            "V": self.validator,
            "S": self.setter,
        }.items():
            if _lambda:
                value = getsource(_lambda)
                if "lambda" in value:
                    value = value.split(sep="lambda")[1].split(sep=":")[1].strip()
                result += f" {key}=~{value}~"
        return result
