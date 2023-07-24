Python - Hello, World

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
- Why Python programming is awesome
- Who is Guido van Rossum
- Who created Python
- Where does the name ‘Python’ come from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using print
- How to use strings
- What are indexing and slicing in Python
- What is the official Holberton Python coding style and how to check your 	code with PEP 8
- Why indentation is so important in Python
- How to use the if, if ... else statements
- How to use comments
- How to affect values to variables
- How to use the while and for loops
- How to use the break and continues statements
- How to use else clauses on loops
- What does the pass statement do, and when to use it
- How to use range
- What does return a function that does not use any return statement
- Scope of variables
- What’s a traceback
- What are the arithmetic operators and how to use them

Requirements
Python Scripts
- Recommended editors: Visual studio code
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using 	   python3 (version 3.4.3)
- All your files should end with a new line
- A README.md file at the root of the alx_python repo, containing a description of the repository
- A README.md file, at the root of the folder of this project, is mandatory
- The length of your files will be tested using wc

TASKS
0. Hello, print
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line. Use the function print

1. Copy - Cut - Paste
Complete this 1-edges.py
- You can find the source code 1-edges.py
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- word_first_3 should contain the first 3 letters of the variable word
- word_last_2 should contain the last 2 letters of the variable word
- middle_word should contain the value of the variable word without the first and last letters

2. Positive anything is better than negative nothing
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.
- You can find the source code 2-pon.py
- The variable number will store a different value every time you will run 	this program
- You don’t have to understand what import, random. randint do. Please do not touch this code
- The output of the program should be:
	-	The number, followed by
		-	if the number is greater than 0: is positive
		-	if the number is 0: is zero
		- 	if the number is less than 0: is negative
	- 	followed by a new line

3. The last digit
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.
-	You can find the source code 3-last_digit.py
-	The variable number will store a different value every time you will run this program
-	You don’t have to understand what import, random.randint do. Please do not touch this code. This -line should not change: number = random.randint(-10000, 10000)
-	The output of the program should be:
	-	The string Last digit of, followed by
	-	the number, followed by
	-	the string is, followed by the last digit of number, followed by
		-	if the last digit is greater than 5: the string and is greater than 5
		-	if the last digit is 0: the string and is 0
		-	if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
	-	followed by a new line

4. Hexadecimal printing
Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)
-	You can only use one print function with string format
-	You can only use one loop in your code
-	You are not allowed to store numbers or strings in a variable
-	You are not allowed to import any module

5. 00...99
Write a program that prints numbers from 0 to 99.
-	Numbers must be separated by ,, followed by a space
-	Numbers should be printed in ascending order, with two digits
-	The last number should be followed by a new line
-	You can only use no more than 2 print functions with string format
-	You can only use one loop in your code
-	You are not allowed to store numbers or strings in a variable
-	You are not allowed to import any module

6. Inventing is a combination of brains and materials. The more brains you use, the less material you need.
-	Write a program that prints all possible different combinations of two digits.
	-	Numbers must be separated by ,, followed by a space	
	-	The two digits must be different
	-	01 and 10 are considered the same combination of the two digits 0 and 1
	-	Print only the smallest combination of two digits
	-	Numbers should be printed in ascending order, with two digits
	-	The last number should be followed by a new line
	-	You can only use no more than 3 print functions with string format
	-	You can only use no more than 2 loops in your code
	-	You are not allowed to store numbers or strings in a variable
	-	You are not allowed to import any module