# coding=utf-8
"""Basic Maths feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('basic_math.feature', 'Some basic math part 1')
def test_some_basic_math_part_1():
    """Some basic math part 1."""


@scenario('basic_math.feature', 'Some basic math part 2')
def test_some_basic_math_part_2():
    """Some basic math part 2."""


@given('I have 1')
def i_have_1():
    """I have 1."""
    return dict(one=1)


@given('I have 5 apples')
def i_have_5_apples():
    """I have 5 apples."""


@when('I add 1 to it')
def i_add_1_to_it(i_have_1):
    """I add 1 to it."""
    i_have_1['one'] += 1


@when('I eat 2 apples')
def i_eat_2_apples():
    """I eat 2 apples."""


@then('I should have 2')
def i_should_have_2(i_have_1):
    """I should have 2."""
    assert i_have_1['one'] == 2


@then('I should have 3 apples')
def i_should_have_3_apples():
    """I should have 3 apples."""

