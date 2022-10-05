import pytest

from pytest_bdd import scenarios, given, when, then, parsers

from main.mapping.Field import Field


class Original:
    def __init__(self):
        self.identifier: str = ""


class Result:
    def __init__(self):
        self.notificationIdentifier: int = 0


class Params:
    def __init__(self):
        self.parameter: str = ""


#@when
def construct_via_fluent_API_with_closure_parameters_and_delegate_help_from_IDE():
    global field
    field = Field[Original, Result, str, int, Params](
        withId=(lambda d, it: 'notificationIdentifier'),
        withGetter=(lambda d, it: it.identifier),
        withValidator=(lambda d, it: it != d.parameters.parameter),
        withDefaulter=(lambda d, it: 777),
        withTranslator=(lambda d, it: int(it)),
        withSetter=(lambda d, it: setattr(d.resultObject, 'notificationIdentifier', it)))
    '''
    field = Field[Original, Result, str, int, Params]
    field.withId(lambda it: 'notificationIdentifier')
    field.withGetter(lambda it: it.identifier)
    field.withValidator(lambda it: it != parameters.parameter)
    field.withDefaulter(lambda it: 777)
    field.withTranslator(lambda it: int(it))
    field.withSetter(lambda it: resultObject.notificationIdentifier = it)
    '''

#@then
def test():
    global field
    assert field.id == "notificationIdentifier"
    assert field.getter
    assert field.validator
    assert field.defaulter
    assert field.translator
    assert field.setter

construct_via_fluent_API_with_closure_parameters_and_delegate_help_from_IDE()
test()