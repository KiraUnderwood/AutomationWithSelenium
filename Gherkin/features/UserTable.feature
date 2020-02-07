Feature: User Table Page Testing

  Background:
    Given a Chrome browser is open

  Scenario: Login
    Given I am on the Home Page
    When I login with epam and 1234
    Then I should see user-icon with PITER CHAILOVSKII reflected


  Scenario Outline: User Table Page test 1
    When I click on "User Table" button in Service dropdown
    Then "User Table" page is opened
    And <dropdown> NumberType Dropdowns are displayed on Users Table on User Table Page
    And <name> User names are displayed on Users Table on User Table Page
    And <img> Description images are displayed on Users Table on User Table Page
    And <txt> Description texts under images are displayed on Users Table on User Table Page
    And <checkbox> checkboxes are displayed on Users Table on User Table Page

    Examples:
    | dropdown | name | img | txt | checkbox |
    |     6    |   6    |  6  | 6   |   6     |

    Scenario Outline: User Table Page test 2
    When I click on "User Table" button in Service dropdown
    Then "User Table" page is opened
    And User table contains following values <number> and <user_name>
    Examples:
    | number | user_name |
    |   1    | Roman |
    |  2     | Sergey Ivan |
    |   3    | Vladzimir |
    |   4    | Helen Bennett |
    |  5     | Yoshi Tannamuri |
    |   6    | Giovanni Rovelli |

    Scenario: User Table Page test 3
    When I click on "User Table" button in Service dropdown
    And I select vip checkbox for "Sergey Ivan"
    Then 1 log row has "Vip: condition changed to true" text in log section

    Scenario Outline: User Table Page test 4
    When I click on "User Table" button in Service dropdown
    And I click on dropdown in column Type for user Roman
    Then Dropdown list contains value <value>
    Examples:
        | value |
        | Admin |
        | User |
        | Manager|









