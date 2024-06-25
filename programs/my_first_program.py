from nada_dsl import *


def perform_computation(int1, int2):
    """
    Perform a computation between two secret integers.
    
    Args:
    int1 (SecretInteger): The first secret integer.
    int2 (SecretInteger): The second secret integer.
    
    Returns:
    SecretInteger: The result of the computation.
    """
    # Example computation: Addition
    # Replace this with any other computation as needed
    result = int1 + int2
    return result


def nada_main():
    try:
        party1 = Party(name="Party1")
        
        # Initialize secret integers
        my_int1 = SecretInteger(Input(name="my_int1", party=party1))
        my_int2 = SecretInteger(Input(name="my_int2", party=party1))
        
        # Perform the desired computation
        computation_result = perform_computation(my_int1, my_int2)
        
        # Return the result as an output
        return [Output(computation_result, "computation_output", party1)]
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    nada_main()
