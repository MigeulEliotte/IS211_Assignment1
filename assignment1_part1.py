# assignment1_part1.py

def list_divide(numbers, divide=2):
    if divide == 0:
        raise ValueError("The divisor cannot be zero.")
    count = sum(1 for num in numbers if num % divide == 0)
    return count

class ListDivideException(Exception):
    pass

def test_list_divide():
    try:
        # Test cases
        assert list_divide([1, 2, 3, 4, 5]) == 2, "Test Case 1 Failed"
        assert list_divide([2, 4, 6, 8, 10]) == 5, "Test Case 2 Failed"
        assert list_divide([30, 54, 63, 98, 100], divide=10) == 2, "Test Case 3 Failed"
        assert list_divide([]) == 0, "Test Case 4 Failed"
        assert list_divide([1, 2, 3, 4, 5], 1) == 5, "Test Case 5 Failed"
    except AssertionError as e:
        raise ListDivideException(f"Assertion error: {e}")

# Call the test function
if __name__ == "__main__":
    test_list_divide()
    print("All test cases passed!")
