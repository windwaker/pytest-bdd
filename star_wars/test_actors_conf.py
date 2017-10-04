# coding=utf-8
"""Star Wars API feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

import pytest
import requests


@scenario('starwars.feature', 'Validating films on a per character basis')
def test_validating_films_on_a_per_character_basis():
    """Validating films on a per character basis."""
    pass


@given('a REST client is pointing to /api/people/1', scope="session")
def a_rest_client_is_pointing_to_apipeople1():
    """a REST client is pointing to /api/people/1."""
    s = requests.Session()
    return s


@given('the user is not authenticated')
def the_user_is_not_authenticated():
    """the user is not authenticated."""
    pass


@pytest.fixture
@when('the GET request is sent')
def the_get_request_is_sent(a_rest_client_is_pointing_to_apipeople1):
    """the GET request is sent."""
    #s = requests.Session()
    r = a_rest_client_is_pointing_to_apipeople1.get('http://swapi.co/api/people/1')
    return r


@then('I should see a list of Luke Skywalker films')
def i_should_see_a_list_of_luke_skywalker_films(the_get_request_is_sent):
    """I should see a list of Luke Skywalker films."""
    assert the_get_request_is_sent.status_code == 200
    assert the_get_request_is_sent.json()["films"] != 0
    


@then('there should be 5 films in the list')
def there_should_be_5_films_in_the_list(the_get_request_is_sent):
    """there should be 5 films in the list."""
    assert len(the_get_request_is_sent.json()["films"]) == 5

