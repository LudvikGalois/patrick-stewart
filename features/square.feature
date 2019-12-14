Feature: Squares

  Scenario: A square starts empty
    Given a square
    Then it is empty

  Scenario: A square becomes occupied
    Given a square
    When I put a piece into it
    Then it is occupied
    And it contains the same piece that I placed

  Scenario: A square can't be occupied twice
    Given a square
    When I put a piece into it
    And I put a piece into it
    Then it throws an OccupiedSquare error
