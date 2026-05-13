# User Story: Create a New Account

**As a** User Service Manager  
**I need** the ability to create a new customer account  
**So that** I can manage customer information in the system  

### Details and Assumptions
* The account must include a unique email address.
* The system should automatically assign a unique ID upon creation.
* The default status of a newly created account should be "Active".

### Acceptance Criteria
```gherkin
Feature: Account Creation

  Scenario: Create a valid account
    Given the service is running and the database is empty
    When I send a POST request to /accounts with a name and email
    Then the response status code should be 201 Created
    And the response body should contain the account ID and name
