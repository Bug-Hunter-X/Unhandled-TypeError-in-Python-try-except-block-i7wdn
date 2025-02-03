def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
except TypeError:
    return "Error: Invalid input type"

#This function is susceptible to a subtle error.
#It catches ZeroDivisionError as expected, but the TypeError is unhandled leading to a silent failure
# This happens when either 'a' or 'b' are not numbers.

# Example
print(function_with_uncommon_error(10, 0))  # Output: Error: Division by zero
print(function_with_uncommon_error(10, "hello")) # Output: Error: Invalid input type
print(function_with_uncommon_error("hello", 10)) #Unhandled error!