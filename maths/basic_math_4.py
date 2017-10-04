# coding=utf-8
"""Basic Maths feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('basic_math_4.feature', 'Some basic math part 4 with scenario outlines')
def test_some_basic_math_part_4_with_scenario_outlines():
    """Some basic math part 4 with scenario outlines."""


@given('there are <start> apples')
def there_are_start_apples(start):
    """there are <start> apples."""
    return dict(start=start)


@when('I eat <eat> apples')
def i_eat_eat_apples(there_are_start_apples, eat):
    """I eat <eat> apples."""
    there_are_start_apples['eat'] = eat


@then('I should have <left> apples')
def i_should_have_left_apples(there_are_start_apples, start, eat, left):
    """I should have <left> apples."""
    assert int(start) - int(eat) == int(left)
    assert there_are_start_apples['start'] == start
    assert there_are_start_apples['eat'] == eat

