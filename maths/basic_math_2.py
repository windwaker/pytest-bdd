# coding=utf-8
"""Basic Maths feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('basic_math_2.feature', 'Some basic math part 2')
def test_some_basic_math_part_2():
    """Some basic math part 2."""


@given('I have 5 apples')
def i_have_5_apples():
    """I have 5 apples."""
    return dict(apples=5)


@when('I eat 2 apples')
def i_eat_2_apples(i_have_5_apples):
    """I eat 2 apples."""
    i_have_5_apples['apples'] -= 2



@then('I should have 3 apples')
def i_should_have_3_apples(i_have_5_apples):
    """I should have 3 apples."""
    assert i_have_5_apples['apples'] == 3


