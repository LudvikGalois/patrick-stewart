Feature: Positions

  Scenario Outline: Valid permissions
    Given "<pos>" as a position
    Then it should be <valid>

    Examples: Positions
      | pos      | valid |
      | 'a1'     | True  |
      | 'A1'     | True  |
      | 'a11'    | False |
      | '1a'     | False |
      | 'b9'     | False |
      | 3        | False |
      | (3,3)    | True  |
      | (8,8)    | False |
      | (3,4,5)  | False |
      | (3,)     | False |
      | 'A0'     | False |
      | None     | False |
      | ('A', 1) | False |
