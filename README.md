## Python Assignment

Question-1 (Finding the Percentage)
```
Import the logging module for logging purposes.
Define the findPercentage function to calculate the average marks for a given student.
Configure logging to display only the message.
Read the number of students' records.
Initialize a dictionary to store student names and their marks.
Loop through each student's record and store their name and marks in the dictionary.
Read the name of the student to query.
Get the marks of the queried student.
Calculate the percentage.
Log the percentage with two decimal places.
Check if the script is executed as the main program and call the findPercentage function.
```

Question-2 (Find the Runner-Up Score!)
```
Define the runnerUp function to find the second largest element in a set.
Import the runnerUp function from the util module.
Read the number of elements in the array.
Read the array elements and map them to integers.
Call the runnerUp function with the set of array elements to find the second largest element.
```

Question-3 (String_Mutation)
```
Define the 'mutate_string' function to replace a character at a given position in a string.
Check if the script is executed as the main program.
Read the original string from input.
Read the position and character to replace from input.
Call the 'mutate_string' function with the original string, position, and character.
Print the modified string.
```

Question-4 (Merge The Tools)
```
Define the merge_the_tools function to split a string into k-sized substrings and remove duplicate characters.
Initialize an empty string to store the result.
Iterate over the string in k-sized steps.
Extract a substring of length k.
Initialize an empty list to store unique characters.
Iterate over characters in the substring.
Add character to the list if not already present.
Append unique characters to the result string.
Add newline character to separate each substring.
Log the result string.
```

Question-5 (Text Alignment)
```
Define the textAlignment function to create a text-based pattern with given thickness.
Initialize an empty string to store the result.
Create the top cone of the pattern.
Create the top pillars of the pattern.
Create the middle belt of the pattern.
Create the bottom pillars of the pattern.
Create the bottom cone of the pattern.
Return the result string.
```

Question-6 (String Formatting)
```
Define the print_formatted function to print formatted numbers in decimal, octal, hexadecimal, and binary formats.
Calculate the width required for formatting based on the number of bits needed to represent the given number in binary.
Iterate through numbers from 1 to the given number+1.
Format and print the numbers in decimal, octal, hexadecimal, and binary formats using string formatting.
Read the ind function.
```

Question-7 (Calendar Module)
```
Import the calendar module for date-related functionalities.
Define the printDay function to print the day of the week for a given date.
Find the day of the week for the given date using the calendar.weekday function.
Define a list of days of the week.
Log and return the day of the week.
```

Question-8 (Collections.namedtuple)
```
Import the namedtuple class from the collections module to define a custom tuple type.
Define the printAverage function to calculate and print the average marks of students.
Read the total number of students.
Define the namedtuple structure for student information.
Extract marks of each student and store in a list.
Calculate the average marks and log it.
Return the average marks.
```

Question-9 (Time Delta)
```
Import the logging module for logging purposes.
Define the time_delta function to calculate the time difference between two timestamps.
Initialize an empty string to store the result.
Configure logging to display only the message.
Import the datetime module for working with date and time.
Parse the input timestamps into datetime objects using the strptime method.
Calculate the absolute difference in seconds between the timestamps.
Convert the difference to an integer and store it as a string.
Log the difference in seconds.
Read the number of test cases.
Iterate through each test case, reading the two timestamps, and calculating the time difference.
```

Question-10 (floor ceil rint)
```
Define the FloorCeilRint function to perform floor, ceil, and rint operations on the input array.
Import the numpy module for array operations.
Call the FloorCeilRint function with the input array, performing floor, ceil, and rint operations.
```

Question-11 (Min Max)
```
import numpy: Import the numpy library for numerical operations.
Read the dimensions of the array (N rows and M columns) from the user.
Create an empty list rows to store the rows of integers.
Iterate over each row:
Read a row of integers from the user.
Split the input string into individual integers.
Convert the integers to integers (from strings).
Add each row to the list of rows.
Convert the list of rows into a numpy array using numpy.array().
Find the minimum value in each row of the array using numpy.min(arr, axis=1) (along the rows), then find the maximum of those minimum values using numpy.max().
Print and return the maximum of the minimum values.
```

Question-12 (Linear Algebra)
```
A function calculate_determinant() to encapsulate the code logic.
User prompts to input the size of the square matrix and its elements.
Calculation of the determinant using numpy.linalg.det().
Printing the determinant rounded to 2 decimal places.
```