# coding=utf-8
"""Basic Maths feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('basic_math_1.feature', 'Some basic math part 1')
def test_some_basic_math_part_1():
    """Some basic math part 1."""


@given('I have 1')
def i_have_1():
    """I have 1."""
    return dict(total=1)


@when('I add 1 to it')
def i_add_1_to_it(i_have_1):
    """I add 1 to it."""
    i_have_1['total'] += 1


@then('I should have 2')
def i_should_have_2(i_have_1):
    """I should have 2."""
    assert i_have_1['total'] == 2

