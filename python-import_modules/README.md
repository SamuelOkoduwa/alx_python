Python - import & modules

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
How to import functions from another file
How to use imported functions
How to create a module
How to use the built-in function dir()
How to prevent code in your script from being executed when imported
How to use command line arguments with your Python programs
What’s the difference between errors and exceptions
What are exceptions and how to use them
When do we need to use exceptions
How to correctly handle an exception
What’s the purpose of catching exceptions
How to raise a builtin exception
When do we need to implement a clean-up action after an exception

Tasks
0. Import a simple function from a simple file
Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3
-	You have to use print function with string format to display integers
-	You have to assign:
	-	the value 1 to a variable called a
	-	the value 2 to a variable called b
	-	and use those two variables as arguments when calling the functions add and print
-	a and b must be defined in 2 different lines: a = 1 and another b = 2
-	Your program should print: <a value> + <b value> = <add(a, b) value> followed with a new line
-	You can only use the word add_0 once in your code
-	You are not allowed to use * for importing or __import__
-	Your code should not be executed when imported - by using __import__, like the example below

1. How to make a script dynamic!
Write a program that prints the number of and the list of its arguments.
-	The output should be:
	-	Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
	-	: (or . if no arguments were passed) followed by
	-	a new line, followed by (if at least one argument),
	-	one line per argument:
		-	the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
-	Your code should not be executed when imported
-	The number of elements of argv can be retrieved by using: len(argv)
-	You do not have to fully understand lists yet, but imagine that argv can be used just like a collection of arguments: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.

2. Everything can be imported
-	Write a program that imports the variable a from the file variable_load_2.py and prints its value.
	-	You are not allowed to use * for importing or __import__
	-	Your code should not be executed when imported

3. Integers division with debug
Write a function that divides 2 integers and prints the result.
-	Prototype: def safe_print_division(a, b):
-	You can assume that a and b are integers
-	The result of the division should print on the finally: section preceded by Inside result:
-	Returns the value of the division, otherwise: None
-	You have to use try: / except: / finally:
-	You have to use "{}".format() to print the result
-	You are not allowed to import any module

4. Raise exception
Write a function that raises a type exception.
-	Prototype: def raise_exception():
-	You are not allowed to import any module

5. Raise a message
Write a function that raises a name exception with a message.
-	Prototype: def raise_exception_msg(message=""):
-	You are not allowed to import any module