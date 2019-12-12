Feature: Piece faces

  Scenario Outline: Parsing a face from a string
     Given the string "<s>"
      When I parse it
      Then I should get <result>

   Examples: String
     | s | result |
     | l | light |
     | L | light |
     | light | light |
     | d | dark |
     | D | dark |
     | dark | dark |
     | black | an error |
     | white | an error |
     | | an error|
