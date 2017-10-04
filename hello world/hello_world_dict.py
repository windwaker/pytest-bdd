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
    return dict(greeting='hello')


@when('it is to the world')
def it_is_to_the_world(i_say_hello):
    """it is to the world."""
    i_say_hello['greeting'] = 'hello world!'


@then('an exclamation point is added')
def an_exclamation_point_is_added(i_say_hello):
    """an exclamation point is added."""
    assert '!' in i_say_hello['greeting'] 

