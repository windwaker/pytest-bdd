# coding=utf-8
"""Basic Maths feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('basic_math_5.feature', 'Some basic math part 5')
def test_some_basic_math_part_5():
    """Some basic math part 5."""


@given('I have <start> <fruits>')
def i_have_start_fruits():
    """I have <start> <fruits>."""


@when('I eat <eat> <fruits>')
def i_eat_eat_fruits():
    """I eat <eat> <fruits>."""


@then('I should have <left> <fruits>')
def i_should_have_left_fruits():
    """I should have <left> <fruits>."""

