# coding=utf-8
"""The simplest example feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('hello_world.feature', 'Hello world!')
def test_hello_world():
    """Hello world!."""


@given('I say hello')
def i_say_hello():
    """I say hello."""
    print('\nhello', end=' ') # default is newline \n


@when('it is to the world')
def it_is_to_the_world():
    """it is to the world."""
    print('world', end='')


@then('an exclamation point is added')
def an_exclamation_point_is_added():
    """an exclamation point is added."""
    print('!')

