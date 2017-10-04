Feature: Basic Maths

    As an person without a calculator
    I want to perform arbitrary mathematical calculations
    So that I can impress my friends at parties


Scenario Outline: Some basic math part 4 with scenario outlines
    Given there are <start> apples
    When I eat <eat> apples
    Then I should have <left> apples

    Examples:
    | start | eat | left |
    |  12   |  5  |  7   |
    |   6   |  3  |  3   |
    |   2   |  1  |  1   |

