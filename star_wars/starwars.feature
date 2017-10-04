Feature: Star Wars API
	# As a [role]
    # I want [feature]
    # So that [benefit]

    # An API that tells us everything we need to know about Star trek :-)
    # Remember what these tests are for: Users, keep micro details for the unit tests

    As an unauthenticated user
    I want to learn about Star Wars
    So that I can impress my friends at parties


Scenario: Validating films on a per character basis
    Given the user is not authenticated
    And a REST client is pointing to /api/people/1
    When the GET request is sent
    Then I should see a list of Luke Skywalker films
    And there should be 5 films in the list

# Scenario: Validating films for a list of users
#     # http://pytest-bdd.readthedocs.io/en/stable/index.html#scenario-outlines
#     Given the user is not authenticated
#     And a REST client is pointing to /api/people/x
#     When the GET request is sent
#     Then I should see a list of all people
#     And each person in that list should be in least one film

# Scenario: Every person should be in at least one film
#     # Loop through each person until you get 404 and then check they have at least one entry present in the films attribute

# Scenario: Every person must have one, and only one, homeworld
#     # Loop through each person until you get 404 and then check they have only one entry present in the homeworld attribute