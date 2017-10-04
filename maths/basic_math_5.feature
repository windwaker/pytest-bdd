Feature: Basic Maths

    As an person without a calculator
    I want to perform arbitrary mathematical calculations
    So that I can impress my friends at parties

    Examples:
    | start | eat | left |
    |  12   |  5  |  7   |
    |  5    |  4  |  1   |

	Scenario: Some basic math part 5
	    Given I have <start> <fruits>
	    When I eat <eat> <fruits>
	    Then I should have <left> <fruits>

	    Examples:
        | fruits  |
        | oranges |
        | apples  |
