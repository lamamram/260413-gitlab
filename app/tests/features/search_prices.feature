@e2e
Feature: check prices
    Tests related to the frontend dawan.fr  
  
    Scenario Outline: verify the prices displayed on the search pages
        Given I get on the home page
        When I type the value $<keyword> in the search input field
        Then I see that the price is $<price>   
        Examples:  
            | keyword  | price |
            | selenium | 1 432 |