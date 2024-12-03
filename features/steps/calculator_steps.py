from behave import given, when, then
from src.calculator import Calculator


@given("I have a calculator")
def init_calculator(context):
    context.calculator = Calculator()


@when("I perform {operation} with {first:d} and {second:d}")
def perform_operation(context, operation, first, second):
    operations = {
        "add": context.calculator.add,
        "subtract": context.calculator.subtract,
        "multiply": context.calculator.multiply,
        "divide": context.calculator.divide,
    }
    context.result = operations[operation](first, second)


@when("I try to divide {number:d} by {divisor:d}")
def divide_numbers(context, number, divisor):
    context.exception = None
    try:
        context.calculator.divide(number, divisor)
    except ValueError as e:
        context.exception = e


@then("the result should be {expected:d}")
def verify_result(context, expected):
    assert context.result == expected, f"Expected {expected}, but got {context.result}"


@then("it should raise a ValueError")
def verify_value_error(context):
    assert isinstance(
        context.exception, ValueError
    ), "Expected ValueError was not raised"
