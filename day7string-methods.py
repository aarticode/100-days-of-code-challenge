#string method in python
def string_operations():
    # Length of the string
    a = "apple"
    print("Length of string:", len(a))

    # Original string
    print("Original string:", a)

    # Uppercase conversion
    print("Uppercase:", a.upper())

    # Lowercase conversion
    print("Lowercase:", a.lower())

    # Stripping characters from the right
    print("Stripped from right:", a.rstrip("!"))

    # Replacing a substring
    print("Replaced:", a.replace("apple", "grapes"))

    # Splitting the string
    print("Split:", a.split(" "))

    # Capitalizing first letter
    blogHeading = "introduction tO python"
    print("Capitalized:", blogHeading.capitalize())

    # Length of a string
    str1 = "Welcome to 100 days of code challenge!!!"
    print("Length of string:", len(str1))

    # Length after centering
    print("Length after centering:", len(str1.center(50)))

    # Counting occurrences of a substring
    print("Count of 'Avocado':", a.count("Avocado"))

    # Checking if a string ends with a particular substring
    str1 = "Welcome to the Console !!!"
    print("Ends with '!!!':", str1.endswith("!!!"))

    # Checking if a substring ends within a specified range
    print("Ends with 'to' between index 4 and 10:", str1.endswith("to", 4, 10))

    # Finding a substring
    str1 = "He's name is Rohit. He is an honest man."
    print("Index of 'ishh':", str1.find("ishh"))

    # Checking if the string is alphanumeric
    str1 = "WelcomeToTheConsole"
    print("Is alphanumeric:", str1.isalnum())

    # Checking if the string is alphabetic
    str1 = "Welcome"
    print("Is alphabetic:", str1.isalpha())

    # Checking if the string is in lowercase
    str1 = "hello world"
    print("Is lowercase:", str1.islower())

    # Checking if the string is printable
    str1 = "We wish you a Merry Christmas\n"
    print("Is printable:", str1.isprintable())

    # Checking if the string contains only whitespace characters
    str1 = "         "       #using Spacebar
    print("Is space:", str1.isspace())
    str2 = "  "       #using Tab
    print("Is space:", str2.isspace())

    # Checking if the string follows title case capitalization
    str1 = "World Health Organization"
    print("Is title case:", str1.istitle())

    # Checking if the string follows title case capitalization
    str2 = "To kill a Mocking bird"
    print("Is title case:", str2.istitle())

    # Checking if the string starts with a specific substring
    str1 = "Python is a Interpreted Language"
    print("Starts with 'Python':", str1.startswith("Python"))

    # Swapping case of the string
    str1 = "Python is a Interpreted Language"
    print("Swapped case:", str1.swapcase())

    # Converting the string to title case
    str1 = "His name is Mohit. Mohit is an honest man."
    print("Title case:", str1.title())

# Call the function
string_operations()
