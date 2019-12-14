Feature: Board

  Scenario: The empty board is empty
    Given an empty board
    Then all squares on the board are empty

  Scenario: The initial board is not empty
    Given the initial board
    Then 4 squares on the board are not empty

  Scenario: Clearing the board
    Given the initial board
    When I clear the board
    Then all squares on the board are empty
