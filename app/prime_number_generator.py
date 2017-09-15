def generate_primes(lower_limit, upper_limit):
    """Function to generate prime numbers from a given interval
    param lower_limit: int variable to store lower limit value
    param upper_limit: int variable to store  upper limit value
    return: list of prime numbers
    """

    if not isinstance(lower_limit, int) or not isinstance(upper_limit, 
      int):
        raise ValueError("Both interval values must be integers")

    if lower_limit < 0 or upper_limit < 0:
        return "all limit intervals must be positive"  