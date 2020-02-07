Feature: Home page and Different Elements page testing

  Background:
    Given a Chrome browser is open

  Scenario: Login
    Given I am on the Home Page
    When I login with epam and 1234
    Then I should see user-icon with PITER CHAILOVSKII reflected

  Scenario Outline: "Service" options in the header
    Given I am on the Home Page
    And I click on "Service" in the header to get the dropdownlist options
    Then I should see <category> subcategory in header:
    Examples:
      | category |
      | Support |
      | Dates |
      | Complex Table |
      | Simple Table |
      | Table With Pages |
      | Different Elements |

  Scenario Outline: "Service" options in the sidebar
    Given I am on the Home Page
    And I click on "Service" in the side nav-bar
    Then I should see  <category> subcategory in sidebar:
    Examples:
      | category |
      | Support |
      | Dates |
      | Complex Table |
      | Simple Table |
      | Table With Pages |
      | Different Elements |

   Scenario Outline: Go to "Different Elements page" and check elements
    Given I am on the Home Page
    And I went to Different Elements page
    Then I should be on Different Elements page
    And I should see <checkboxes> checkboxes
    And I should see <radiobuttons> radiobuttons
    And I should see <dropdown> dropdown list
    And I should see <buttons> buttons
    Examples:
       | checkboxes | radiobuttons | dropdown | buttons |
       |    4       |   4          |   1      |   2     |

   Scenario Outline: Check logs for checkboxes
    Given I went to Different Elements page
    When I select <checkbox> checkbox
    Then I should see corresponding log
    Examples:
       | checkbox |
       | Water |
       | Wind |

   Scenario Outline: Check logs for radiobutton
    Given I went to Different Elements page
    When I select <radio> radiobutton
    Then I should see corresponding log
    Examples:
       | radio |
     | Selen |


   Scenario Outline: Check logs for dropdownlist
    Given I went to Different Elements page
    When I select <opt> from dropdown
    Then I should see corresponding log
    Examples:
       | opt |
       | Yellow |

   Scenario: Check logs after un-ticking all checkboxes
    Given I went to Different Elements page
    When I un-tick all checkboxes
    Then I should see corresponding log








