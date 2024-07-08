from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Basic arithmetic operations
    sum_result = my_int1 + my_int2
    product_result = my_int1 * my_int2
    difference_result = my_int1 - my_int2
    quotient_result = my_int1 / my_int2

    # Conditional logic
    max_result = (my_int1 < my_int2).if_else(my_int2, my_int1)

    # A custom function using the @nada_fn decorator
    @nada_fn
    def custom_operation(a: SecretInteger, b: SecretInteger) -> SecretInteger:
        return (a + b) * (a - b)

    custom_result = custom_operation(my_int1, my_int2)

    # Function to calculate the square of a number
    @nada_fn
    def square(a: SecretInteger) -> SecretInteger:
        return a * a

    square_result1 = square(my_int1)
    square_result2 = square(my_int2)

    # Function to compute the maximum of three numbers
    @nada_fn
    def max_of_three(a: SecretInteger, b: SecretInteger, c: SecretInteger) -> SecretInteger:
        return (a < b).if_else(
            (b < c).if_else(c, b),
            (a < c).if_else(c, a)
        )

    max_of_three_result = max_of_three(my_int1, my_int2, square_result1)

    # Return all results as outputs
    return [
        Output(sum_result, "sum_output", party1),
        Output(product_result, "product_output", party1),
        Output(difference_result, "difference_output", party1),
        Output(quotient_result, "quotient_output", party1),
        Output(max_result, "max_output", party1),
        Output(custom_result, "custom_output", party1),
        Output(square_result1, "square_output1", party1),
        Output(square_result2, "square_output2", party1),
        Output(max_of_three_result, "max_of_three_output", party1)
    ]
