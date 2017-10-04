# coding=utf-8
"""Star Wars API feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('starwars.feature', 'Some basic math')
def test_some_basic_math():
    """Some basic math."""


@given('I have 5 apples')
def i_have_5_apples():
    """I have 5 apples."""
    return dict(have=5)


@when('I eat 2 apples')
def i_eat_2_apples(i_have_5_apples):
    """I eat 2 apples."""
    i_have_5_apples['eat'] = 2


@then('I should have 3 apples')
def i_should_have_3_apples(i_have_5_apples):
    """I should have 3 apples."""
    assert i_have_5_apples['have'] - i_have_5_apples['eat'] == 3

