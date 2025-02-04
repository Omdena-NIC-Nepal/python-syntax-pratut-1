def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    fromated_str = f"My name is {name} and I am {age} years old"
    return fromated_str

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"

    """
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    elif number == 10:
        return "Equal"

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    count = 0  # Initialize sum
    for i in range(1, n + 1):  # Loop from 1 to n
        count += i  # Add i to count
    return count  # Return the total sum

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    sum_num = sum(numbers)  # Direct sum calculation
    max_num = max(numbers)  # Maximum value
    min_num = min(numbers)  # Minimum value

    return (sum_num, max_num, min_num)

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    filtered_students = []
    for name, score in students_dict.items():
        if score >= 80:
            filtered_students.append(name)
    return filtered_students

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    list1 = set(list1)
    list2 = set(list2)
    return list1 & list2

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    return{
        "sum" : a + b,
        "difference": a-b, 
        "product": a*b, 
        "quotient": a/b
    }

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    return {
        "and": x and y,      
        "or": x or y,        
        "not_x": not(x or y)       
    }

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return {
        "and": a & b,       # Bitwise AND
        "or": a | b,        # Bitwise OR
        "xor": a ^ b,       # Bitwise XOR
        "NOT a": ~a,        # Bitwise NOT of a
        "NOT b": ~b,        # Bitwise NOT of b
        "Left Shift a": a << 1,  # Left shift a by 1
        "Left Shift b": b << 1,  # Left shift b by 1
        "Right Shift a": a >> 1,  # Right shift a by 1
        "Right Shift b": b >> 1   # Right shift b by 1
    }
