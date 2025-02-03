def function_with_uncommon_error(a, b):
    try:
        if not isinstance(a,(int, float)) or not isinstance(b,(int,float)):
            raise TypeError("Inputs must be numbers")
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError as e:
        return f"Error: {e}"

# Example
print(function_with_uncommon_error(10, 0))  # Output: Error: Division by zero
print(function_with_uncommon_error(10, "hello"))  # Output: Error: Inputs must be numbers
print(function_with_uncommon_error("hello", 10))  # Output: Error: Inputs must be numbers