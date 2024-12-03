Feature: Calculator
  As a user
  I want to perform basic arithmetic operations
  So that I can get correct calculations

  Scenario Outline: Basic arithmetic operations
    Given I have a calculator
    When I perform <operation> with <first> and <second>
    Then the result should be <result>

    Examples: Addition
      | operation | first | second | result |
      | add      | 5     | 3      | 8      |
      | add      | -2    | 7      | 5      |

    Examples: Subtraction
      | operation | first | second | result |
      | subtract  | 10    | 4      | 6      |
      | subtract  | 2     | 8      | -6     |

    Examples: Multiplication
      | operation | first | second | result |
      | multiply  | 4     | 3      | 12     |
      | multiply  | -5    | 4      | -20    |

    Examples: Division
      | operation | first | second | result |
      | divide    | 10    | 2      | 5      |
      | divide    | 15    | 3      | 5      |

  Scenario: Division by zero
    Given I have a calculator
    When I try to divide 10 by 0
    Then it should raise a ValueError
