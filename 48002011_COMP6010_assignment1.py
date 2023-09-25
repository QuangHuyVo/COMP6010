# Student Declaration
# I [Quang Huy Vo - 48002011] declare that this is my own work and that
# I have not used any code or logic from other people or from sources outside of the unit. 
# I understand that it is ok to look at COMP6010 videos and COMP6010 resources
# and that researching how certain python operators / functions work is ok.
# [x] <== put an x in here to indicate you have read and agree to the above statements.

# IMPORTANT !!!
# DO NOT MODIFY ANY FUNCTION HEADERS

# your mission is to complete function1 to function10.
# a main function is provided at the bottom of the file with sample test data. This sample test data is not exhaustive.
# you may modify the main function to test other input values to ensure the correctness of your program

def function1(string_to_process):
    """
    Reverse String:
    takes a string as an input
    returns the string with the characters in reverse.
    if the input is not a valid string, then return an empty string ""
    e.g.
    function1("Hello2023") will return "3202olleH"
    function1(556) will return ""
    """
    # TODO add code here
    if type(string_to_process) == str:
        return string_to_process[::-1]
    else:
        return "" 


def function2(string_to_process):
    """
    First Character of each word:
    takes a string as input
    returns the string with the first character of each word (including numbers / other characters)
    if the input is not a valid string, then return an empty string ""
    e.g.
    function2("Hi there bob") will return "Htb" as a string
    function2("Hi there agent 86, how are you today?") will return "Hta8hayt" as a string
    """
    # TODO add code here
    if type(string_to_process) == str:
        first_chars = "" 
        split = string_to_process.split()

        for i in split:
            if len(i) > 0:
                first_chars += i[0]
        return first_chars
    else:
        return "" 

def function3(string_to_process):
    """
    Sum of ASCII values:
    using the inbuilt ord() function to get the ascii value of a character, add up all the ascii values of the individual characters in the string
    if the input is not a valid string, then return 0 ... the integer zero (not the string "0")
    e.g.
    function3("A") returns 65
    function3("Aa") returns 162   ... that is the result of 65+97
    """
    # TODO add code here
    if type(string_to_process) == str:
        sum = 0

        for i in string_to_process:
            value = ord(i)
            sum += value
        return sum
    else:   
        return "" 


def function4(the_integer, the_float, the_other_string):
    """
    Careful printing format: (you may assume valid inputs for this function)
    Given three inputs, carefully format the output to match the examples (printing on a single line):
    e.g.1: function4(5, 6.3, "Week") will return the following string (without quotes)...
    "5 // 2 = 2, the closest integer to 6.3 is 6, and the word "Week" is 4 characters long."

    e.g.2: function4(0, 5.0, "") will return the following string (without quotes)...
    "0 // 2 = 0, the closest integer to 5.0 is 5, and the word "" is 0 characters long."

    e.g.3: function4(0, 5.6, "") will return the following string (without quotes)...
    "0 // 2 = 0, the closest integer to 5.6 is 6, and the word "" is 0 characters long."
    """
    # TODO add code here
    if type(the_integer) == int and type(the_float) == float and type(the_other_string) == str:
    
        rounded = round(the_float)
        length = len(the_other_string)
        output = str(the_integer) + " // 2 = " + str(the_integer // 2) + ", the closest integer to " + str(the_float) + " is " + str(rounded) + ', and the word "' + the_other_string + '"'  " is " + str(length) + " characters long."
    return output


def function5(string_to_process):
    """
    Filter out vowels:
    You can assume a valid string is given as a parameter (no need for error checking). 
    Filter out any english vowel from the string and return the updated string
    e.g. function5("Hi There") will return "H Thr"
    e.g. function5("aaaaaaaa") will return ""
    """
    # TODO add code here
    vowels = "aeiouAEIOU"
    output = ""

    for i in string_to_process:
        if i not in vowels:
            output += i

    return output


def function6(string_to_process):
    """
    The "COMP6010 lucky number" of a string:
    take the string and calculate the highest ascii value within the string.
    take that highest value and divides the number by the length of the string.
    if you are given a string of length 0, return -1
    e.g. function6("A") would return 65 / 1 = 65
    e.g. function6("AA") would return 65 / 2 = 32.5
    e.g. function6("Aa") would return 97 / 2 = 48.5
    e.g. function6("") would return -1
    """
    # TODO add code here
    if len(string_to_process) == 0:
        return -1
    
    highest = 0

    for i in string_to_process:
        value = ord(i)
        if value > highest:
            highest = value
    COMP6010_lucky_number = highest / len(string_to_process)

    return COMP6010_lucky_number


def function7(string_1_to_process, string_2_to_process, string_3_to_process):
    """
    Calculate the COMP6010 lucky number of each given string
    Then return a string that concatenates all strings together in the order from lowest to highest lucky number.
    e.g. function7("A","a","Z") will return "AZa"
    e.g. function7("A","aaa","Z") will return "aaaAZ"
    e.g. function7("A","A","A") will return "AAA"
    e.g. function7("A","A","") will return "AA"
    """
    # TODO add code here
    lucky1 = function6(string_1_to_process)
    lucky2 = function6(string_2_to_process)
    lucky3 = function6(string_3_to_process)

    if lucky1 > lucky2 > lucky3:
        output = string_3_to_process + string_2_to_process + string_1_to_process
    elif lucky2 > lucky3 > lucky1:
        output = string_1_to_process + string_3_to_process + string_2_to_process
    elif lucky3 > lucky1 > lucky2: 
        output = string_2_to_process + string_1_to_process + string_3_to_process
    elif lucky1 > lucky3 > lucky2:
        output = string_2_to_process + string_3_to_process + string_1_to_process
    elif lucky2 > lucky1 > lucky3:
        output = string_3_to_process + string_1_to_process + string_2_to_process
    elif lucky3 > lucky2 > lucky1:
        output = string_1_to_process + string_2_to_process + string_3_to_process
    return output


def function8(string_to_process):
    """
    Apply a special invert:
    For each character in the string, 
    - if it is lower case, make it upper case
    - if it is upper case, make it lower case
    - if it is a digit (0 to 9) then make it make it 9 minus the digit
    e.g. function8("Hello there agent 86") returns "hELLO THERE AGENT 13"
    e.g. function8("Hello there agent 86!") returns "hELLO THERE AGENT 13!"
    """
    # TODO add code here
    output = ""
    for i in string_to_process:
        if i.islower():
            output += i.upper()
        elif i.isupper():
            output += i.lower()
        elif i in range (9):
            output += str(9- int(i))
        else: 
            output += i
    return output

def function9(positive_integer_to_process):
    """
    We discussed the collatz conjecture in the week 3 lecture recording and gave you an algorithm.
    Given a positive integer:
    step 1:
    if the number is 1, then return 0
    step 2: 
    if the number is even, divide by 2
    else multiply it by 3 and add 1
    step 3: check if the new number is == 1... if it is not, then apply step 2 again until the number is 1

    The collatz number is the number of times you need to run step 2.
    for instance, the collatz numbers are listed below for the first 10 positive integers
    function9( 1 ) returns 0
    function9( 2 ) returns 1
    function9( 3 ) returns 7
    function9( 4 ) returns 2
    function9( 5 ) returns 5
    function9( 6 ) returns 8
    function9( 7 ) returns 16
    function9( 8 ) returns 3
    function9( 9 ) returns 19

    This function should return the Collatz number for the given integer
    """
    # TODO add code here
    if positive_integer_to_process == 1:
        return 0 
    col_num = 0

    while positive_integer_to_process != 1:
        if positive_integer_to_process % 2 == 0:
            positive_integer_to_process = positive_integer_to_process / 2
        else: 
            positive_integer_to_process = (positive_integer_to_process * 3) + 1
        col_num += 1 
    return col_num


def function10(integer_to_process):
    """
    Closest Fibonacci number:
    The Fibonacci numbners are a sequence starting 1, 1, ... that follow a calculation.
    The next number is the sum of the previous 2 numbers.
    so the first 10 numbers are:
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

    return the closest Fibonacci number to the passed value
    e.g. function10(1) returns 1
    e.g. function10(5) returns 5
    e.g. function10(7) returns 8
    e.g. function10(0) returns 1
    e.g. function10(1000) returns 987
    """
    # TODO add code here
    a, b = 1, 1
    if integer_to_process <= 0:
        return 1
    if integer_to_process == 1:
        return 1
    
    while True:
        c = a + b
        if c > integer_to_process:
            if abs(integer_to_process - b) <  abs(integer_to_process - c):
                return b
            else: 
                return c
        a, b = b, c 

    


# IMPORTANT !!!
# DO NOT MODIFY ANY FUNCTION HEADERS

# your mission is to complete function1 to function10.
# a main function is provided at the bottom of the file with sample test data. This sample test data is not exhaustive.
# you may modify the main function to test other input values to ensure the correctness of your program


def main():
    """
    You may comment or uncomment any of the following function calls to test specific functions.
    You may also add your own test data as part of main function to check if your functions can handle
    all inputs.
    """
    print(function1("Hello2023"))
    print(function2("Hi there agent 86, how are you today?"))
    print(function3("Aa"))
    print(function4(5, 6.3, "Week"))
    print(function5("Hi There"))
    print(function6("Aa"))
    print(function7("A","aaa","Z"))
    print(function8("Hello there agent 86!"))
    print(function9(3))
    print(function10(5))
    

if(__name__ == "__main__"):
    main()