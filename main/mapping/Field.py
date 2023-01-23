# *
#    Descriptor of a field mapping.
#    <p>
#    Intended to be constructed using fluid API and method chaining.
#    Example:
#    <code><pre>
#        new Field&lt;Map&lt;String,?&gt;,Event,String,Long&gt;().
#            withId('notificationIdentifier').
#            withGetter {it.identifier}.
#            withTranslator {Long.parseLong(it)}.
#            withSetter { resultObject.notificationIdentifier=it }* </pre></code>
#    <p>
#    OO - Original object type.
#    RO - Resulting object type.
#    OF - Original field type.
#    RF - Resulting field type.
#    P - Type of parameters object.
#
from typing import Generic, TypeVar, Callable, Optional

import logging

logger = logging.getLogger(__name__)

OO = TypeVar("OO")
RO = TypeVar("RO")
OF = TypeVar("OF")
RF = TypeVar("RF")
P = TypeVar("P")


class Field(Generic[OO, RO, OF, RF, P]):
    """
    Descriptor of a field mapping.

    Intended to be constructed using fluid API and method chaining.
    Example:
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
        """
        :param withId:         Identifier of field.
                               Used for debugging and testing purposes.

        :param withGetter:     Gets field value from original object.

        :param withValidator:  Verifies field value from original object.

        :param withTranslator: Translates field value from original object to format of result object.

        :param withSetter:     Injects translated field value into result object.

        :param withDefaulter:  Gets field value in case it was not set in original object.
        """
        assert withId
        self.id = withId
        self.getter = withGetter
        self.validator = withValidator
        self.translator = withTranslator
        self.setter = withSetter
        self.defaulter = withDefaulter
        logger.debug(self)

    def __str__(self) -> str:
        import inspect

        result = self.id
        for key, _lambda in {
            "G": self.getter,
            "D": self.defaulter,
            "T": self.translator,
            "V": self.validator,
            "S": self.setter,
        }.items():
            if _lambda:
                value = inspect.getsource(_lambda)
                if "lambda" in value:
                    value = value.split(sep="lambda")[1].split(sep=":")[1].strip()
                result += f" {key}=~{value}~"
        return result
