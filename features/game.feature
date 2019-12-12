Feature: Playing a game

  Scenario: Creating a game
    Given we have a new game
     Then there is a light piece at d4
      And there is a dark piece at e4
      And there is a dark piece at d5
      And there is a light piece at e5
