# coding=utf-8
"""Basic Maths feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)


@scenario('basic_math_3.feature', 'Some basic math part 3')
def test_some_basic_math_part_3():
    """Some basic math part 3."""


#@given('I have 5 apples')
@given(parsers.parse('I have {start:d} apples'))
def i_have_5_apples(start):
    """I have 5 apples."""
    return dict(start=start, eat=0)


#@when('I eat 2 apples')
@when(parsers.parse('I eat {eat:d} apples'))
def i_eat_2_apples(i_have_5_apples, eat):
    """I eat 2 apples."""
    i_have_5_apples['eat'] += eat


#@then('I should have 3 apples')
@then(parsers.parse('I should have {left:d} apples'))
def i_should_have_3_apples(i_have_5_apples, start, eat, left):
    """I should have 3 apples."""
    assert i_have_5_apples['start'] == start
    assert i_have_5_apples['eat'] == eat
    assert start - i_have_5_apples['eat'] == left
