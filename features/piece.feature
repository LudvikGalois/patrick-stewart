Feature: Pieces

  Scenario Outline: Flipping a piece
     Given a <colour> piece
      When I flip it <n> time(s)
      Then it should be a <result> piece
       and the flip count should be <n>

   Examples: Flips
     | colour | n | result |
     | light  | 0 | light  |
     | dark   | 0 | dark   |
     | light  | 1 | dark   |
     | dark   | 1 | light  |
     | light  | 2 | light  |
     | dark   | 2 | dark   |
     | light  | 3 | dark   |
     | dark   | 3 | light  |
